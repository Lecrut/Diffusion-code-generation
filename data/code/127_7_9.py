def is_odd(num):
    return num & 1

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    odd_numbers = [num for num in sample_numbers if is_odd(num)]
    print(f"Odd numbers: {odd_numbers}")