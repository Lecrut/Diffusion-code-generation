def remove_spaces(input_list):
    return [item.replace(" ", "") for item in input_list]

if __name__ == '__main__':
    sample_list = ["Hello World", "This is a test string", "Python programming"]
    result = remove_spaces(sample_list)
    print(result)