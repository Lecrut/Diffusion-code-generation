if __name__ == '__main__':
    numbers = range(1, 101)
    divisible_by_3_and_5 = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
    print(divisible_by_3_and_5)