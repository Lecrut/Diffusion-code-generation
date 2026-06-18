def extract_first_letters(words):
    return [word[0].upper() for word in words if len(word) > 0]
if __name__ == '__main__':
    sample_input = "hello world python script execution"
    words_list = sample_input.split()
    result = extract_first_letters(words_list)
    print("".join(result))