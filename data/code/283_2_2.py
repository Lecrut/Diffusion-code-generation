def filter_python_strings(string_list):
    return [s for s in string_list if 'Python' in s]
if __name__ == '__main__':
    sample_list = ["Hello Python world", "Java programming", "Python is fun", "C++ development", "Another Python example"]
    result = list(filter_python_strings(sample_list))
    print(result)