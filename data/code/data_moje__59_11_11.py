def digit_sum(n):
    n = abs(int(n))
    total = 0
    for char in str(n):
        total += int(char)
    return total

if __name__ == '__main__':
    sample_values = [0, 123, 999, 1000000000000000000, 123456789012345678]
    for value in sample_values:
        print(digit_sum(value))