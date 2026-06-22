def join_strings(string_list):
    return ''.join(string_list)

if __name__ == '__main__':
    sample_strings = ["Hello", " ", "World", "!"]
    result = join_strings(sample_strings)
    print(result)