def decimal_to_binary(number: int) -> str:
    if number < 0:
        raise ValueError("Only positive integers are allowed")
    return f'{number:b}'

if __name__ == '__main__':
    sample_values = [0, 1, 10, 255, 1024, 65535]
    for value in sample_values:
        print(decimal_to_binary(value))