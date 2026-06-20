def is_odd_number(num):
    return num & 1 == 1

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    odd_count = sum(is_odd_number(num) for num in sample_numbers)
    print(odd_count % 2 == 0 and "Even number of odd numbers." or "Odd number of odd numbers.")