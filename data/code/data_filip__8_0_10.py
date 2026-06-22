def split_commas(input_str: str) -> list[str]:
    return [part for part in input_str.split(',') if part]

if __name__ == '__main__':
    sample_input = "apple, banana, , grape, , kiwi"
    result = split_commas(sample_input)
    print(result)