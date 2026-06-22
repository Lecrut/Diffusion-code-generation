def convert_kilometers_to_meters(kilometers: int) -> int:
    return kilometers * 1000

if __name__ == '__main__':
    sample_input = 5
    result = convert_kilometers_to_meters(sample_input)
    print(result)