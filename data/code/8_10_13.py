def split_and_trim(input_string: str) -> list:
    if not input_string:
        return []
    parts = input_string.split(',')
    result = [part.strip() for part in parts if part.strip()]
    return result

if __name__ == '__main__':
    sample_input = "  hello ,  world  , , foo  ,  bar  ,  "
    result = split_and_trim(sample_input)
    print(result)