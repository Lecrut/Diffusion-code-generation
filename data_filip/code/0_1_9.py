def filter_and_join_numbers(input_string):
    return ''.join([char for char in input_string if char.isdigit()])

if __name__ == '__main__':
    sample_text = "abc123def45ghi678"
    result = filter_and_join_numbers(sample_text)
    print(result)