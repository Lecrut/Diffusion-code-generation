def extract_first_letters(text: str) -> str:
    words = text.split()
    result = [word[0] for word in words if len(word) > 0]
    return ''.join(result).upper()
if __name__ == '__main__':
    user_input = "Hello World Python Programming"
    processed_output = extract_first_letters(user_input)
    print(processed_output)