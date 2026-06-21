def decimal_to_binary_string(number: int) -> str:
    return f"{number:b}"

if __name__ == '__main__':
    sample_number = 42
    result = decimal_to_binary_string(sample_number)
    print(result)