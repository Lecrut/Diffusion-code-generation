def decimal_to_binary(n: int) -> str:
    if n <= 0:
        return "0"
    result = ""
    temp = n
    while temp > 0:
        result = str(temp % 2) + result
        temp //= 2
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 15, 255]
    for value in sample_values:
        print(decimal_to_binary(value))