def reverse_integer(n):
    sign = -1 if n < 0 else 1
    digits = [d for d in str(abs(n))]
    digits.reverse()
    reversed_num = int("".join(digits)) * sign
    return reversed_num

if __name__ == "__main__":
    test_values = [123, -456, 700, 0, 1534236469]
    for value in test_values:
        print(reverse_integer(value))