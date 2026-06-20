def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    sample_numbers = [3, 4, -5, 0]
    for num in sample_numbers:
        print(is_odd(num))