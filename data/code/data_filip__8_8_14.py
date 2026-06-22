def split_and_clean(input_str):
    return [item.strip() for item in input_str.split(',') if item.strip()]

if __name__ == '__main__':
    sample_input = "  hello , , world ,  python  ,  "
    result = split_and_clean(sample_input)
    print(result)