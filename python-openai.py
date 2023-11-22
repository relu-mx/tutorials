import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

def text_completion():
    # Text Completion example
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Once upon a time",
        max_tokens=50
    )
    print("Text Completion:")
    print(response.choices[0].text.strip())
    print()

def text_classification():
    # Text Classification example
    response = openai.Classification.create(
        model="text-davinci-003",
        examples=[
            ["A happy moment", "Positive"],
            ["I am sad.", "Negative"],
            ["It's a sunny day", "Neutral"]
        ],
        query="It's raining outside"
    )
    print("Text Classification:")
    print(response.label)
    print()

def main():
    text_completion()
    text_classification()

if __name__ == "__main__":
    main()
