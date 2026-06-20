def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    test_numbers = [1, -2, 5, -8, 3]
    for num in test_numbers:
        print(f"{num} is odd: {is_odd(num)}")