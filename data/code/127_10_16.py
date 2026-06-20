def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    sample_numbers = [3, 4, 7, 8, 11, 12]
    for num in sample_numbers:
        print(f"The number {num} is {'Odd' if is_odd(num) else 'Even'}")