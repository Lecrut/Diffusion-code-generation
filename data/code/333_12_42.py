def extract_first_letters(words):
    return [word[0].upper() for word in words if len(word) > 0]
if __name__ == '__main__':
    user_input = ["hello", "world", "python", "programming"]
    result = extract_first_letters(user_input)
    print("".join(result))