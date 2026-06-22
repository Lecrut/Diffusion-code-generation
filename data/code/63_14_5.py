def reverse_integer(n):
    sign = -1 if n < 0 else 1
    digits = [d for d in str(abs(n))]
    reversed_digits = digits[::-1]
    result = int("".join(reversed_digits)) * sign
    return result

if __name__ == "__main__":
    test_values = [123, -456, 1200, 0]
    for value in test_values:
        print(reverse_integer(value))