def join_strings(string_list):
    return ''.join(string_list)

if __name__ == '__main__':
    sample_values = ["Hello", " ", "World", "!"]
    result = join_strings(sample_values)
    print(result)