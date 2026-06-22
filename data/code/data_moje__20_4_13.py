def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 10, 11]
    for value in values:
        print(is_even(value))