def is_divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0

if __name__ == '__main__':
    for i in range(1, 101):
        if is_divisible_by_3_and_5(i):
            print(i)