def get_first_letters(input_string):
    return [word[0] for word in input_string.split() if word]

if __name__ == '__main__':
    sample_input = "Hello world from Alibaba Cloud"
    result = get_first_letters(sample_input)
    print(result)