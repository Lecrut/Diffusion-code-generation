ODD_THRESHOLD = 1

def is_odd(number):
    return number % 2 != ODD_THRESHOLD

if __name__ == '__main__':
    test_numbers = [5, -10, 0, 3, -7]
    for num in test_numbers:
        print(f"{num} is odd: {is_odd(num)}")