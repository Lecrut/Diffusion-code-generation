def lowercase_list(string_list):
    return [s.lower() for s in string_list]
if __name__ == '__main__':
    sample_list = ["Hello", "World", "Python", "List Comprehension"]
    result = lowercase_list(sample_list)
    print(result)