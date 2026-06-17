def filter_strings(string_list):
    return [s for s in string_list if 'Python' in s]
if __name__ == '__main__':
    sample_list = ["Hello Python world", "Java programming", "Python is fun", "C++ code"]
    result = list(filter_strings(sample_list))
    print(result)