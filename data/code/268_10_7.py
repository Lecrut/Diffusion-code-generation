def find_first_word(s):
    return s.split()[0]

if __name__ == '__main__':
    sample_string = "Hello world from Qwen"
    print(find_first_word(sample_string))