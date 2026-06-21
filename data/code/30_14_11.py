def decimal_to_binary(n: int) -> str:
    return f'{n:b}'

if __name__ == '__main__':
    sample_values = [0, 1, 10, 255, 1024, 65535]
    for val in sample_values:
        print(decimal_to_binary(val))