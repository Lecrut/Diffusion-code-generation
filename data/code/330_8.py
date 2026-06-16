def convert_to_uppercase(string_list):
    return [s.upper() for s in string_list]
if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "code"]
    result = convert_to_uppercase(sample_list)
    print(result)