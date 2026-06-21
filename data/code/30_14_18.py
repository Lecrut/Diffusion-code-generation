def to_binary_string(n: int) -> str:
    if n <= 0:
        raise ValueError('Input must be a positive integer')
    return f'{n:b}'
if __name__ == '__main__':
    sample_values = [1, 2, 5, 10, 255, 1024]
    for value in sample_values:
        result = to_binary_string(value)
        print(result)