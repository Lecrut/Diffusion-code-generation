def string_to_char_list(s):
    return [s[i] for i in range(len(s))]

if __name__ == '__main__':
    sample_string = "hello"
    print(string_to_char_list(sample_string))