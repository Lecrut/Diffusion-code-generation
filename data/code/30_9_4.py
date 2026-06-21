def int_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    bits.reverse()
    return "".join(bits)

if __name__ == "__main__":
    sample_values = [0, 1, 5, 10, 15, 255, 1024]
    for value in sample_values:
        result = int_to_binary(value)
        print(result)