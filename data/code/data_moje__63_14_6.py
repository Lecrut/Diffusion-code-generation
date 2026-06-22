def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_str = ''.join([c for c in str(abs(n))][::-1])
    return sign * int(reversed_str)

if __name__ == '__main__':
    sample_values = [123, -456, 0, 1200]
    for val in sample_values:
        print(reverse_integer(val))