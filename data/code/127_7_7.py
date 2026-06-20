def is_odd(num):
    return num & 1

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    odd_count = sum(is_odd(num) for num in sample_numbers)
    print("Number of odd numbers:", odd_count)