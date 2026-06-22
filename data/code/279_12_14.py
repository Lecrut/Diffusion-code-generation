def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    for num in range(100):
        if is_even(num):
            print(num)