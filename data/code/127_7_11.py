def is_odd(number):
    return number & 1

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    odd_count = sum(is_odd(num) for num in sample_numbers)
    if odd_count % 2 == 0:
        print("Even number of odd numbers.")
    else:
        print("Odd number of odd numbers.")