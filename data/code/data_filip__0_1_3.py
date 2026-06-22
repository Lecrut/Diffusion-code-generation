def extract_and_join_numbers(text):
    return "".join([char for char in text if char.isdigit()])

if __name__ == '__main__':
    sample_string = "abc123def45gh678"
    result = extract_and_join_numbers(sample_string)
    print(result)