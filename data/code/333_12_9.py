def extract_first_letters(words):
    result = []
    for word in words:
        if len(word) > 0 and not word[0].isspace():
            initial = word[0]
            if 'a' <= initial.lower() <= 'z':
                result.append(initial.upper())
    return ''.join(result)
if __name__ == '__main__':
    sample_input = "hello world python script"
    words_list = sample_input.split()
    output_string = extract_first_letters(words_list)
    print(output_string)