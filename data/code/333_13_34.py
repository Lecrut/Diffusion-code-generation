import sys
def extract_first_letters(text):
    return [word[0].lower() for word in text.split() if len(word) > 1]
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = extract_first_letters(sample_input)
    print("".join(result))