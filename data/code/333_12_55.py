def extract_first_letters(text):
    words = text.split()
    return ''.join(word[0].lower() for word in words)
if __name__ == '__main__':
    user_input = "Hello World This Is A Test"
    result = extract_first_letters(user_input)
    print(result)