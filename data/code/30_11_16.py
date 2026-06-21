def decimal_to_binary(n: int) -> str:
    return format(n, 'b')

if __name__ == '__main__':
    value = 42
    result = decimal_to_binary(value)
    print(result)