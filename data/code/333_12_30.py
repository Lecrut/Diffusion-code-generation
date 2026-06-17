words = ["hello", "world", "this", "is", "a"]
def extract_first_letters(word_list):
    result = ""
    for word in word_list:
        if len(word) > 0:
            letter = word[0].upper()
            result += letter
    return result
if __name__ == '__main__':
    output_string = extract_first_letters(words)
    print(output_string)