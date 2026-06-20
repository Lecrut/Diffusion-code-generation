def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    test_numbers = [21, 34, 56, 78, 90]
    for num in test_numbers:
        print(f"The number {num} is odd: {is_odd(num)}")