def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    test_numbers = [-5, 10, 3, -8, 1]
    for num in test_numbers:
        print(f"{num} is odd: {is_odd(num)}")