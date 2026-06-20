def split_by_comma(input_str):
    return [part.strip() for part in input_str.split(',') if part.strip()]

if __name__ == '__main__':
    sample = "  apple , banana ,, orange  ,  ,grape"
    result = split_by_comma(sample)
    print(result)