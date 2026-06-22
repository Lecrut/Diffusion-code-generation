def remove_spaces(input_list):
    return [s.replace(" ", "") for s in input_list]

if __name__ == '__main__':
    sample_values = ["Hello World", "This is a test string", "Remove spaces"]
    result = remove_spaces(sample_values)
    print(result)