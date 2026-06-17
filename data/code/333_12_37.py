def extract_first_letters(text: str) -> str:
    words = text.split()
    return ''.join(word[0].lower() for word in words if word.strip())
if __name__ == '__main__':
    user_input = "Hello World Python Programming"
    result = extract_first_letters(user_input)
    print(result)