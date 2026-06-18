def extract_first_letters(text: str) -> str:
    words = text.split()
    return ''.join(word[0].upper() for word in words if word)
if __name__ == '__main__':
    user_input = "hello world this is a test"
    result = extract_first_letters(user_input)
    print(result)