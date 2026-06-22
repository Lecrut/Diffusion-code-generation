def sum_of_nine_integers():
    numbers = (i for i in range(1, 10))
    return sum(numbers)

if __name__ == '__main__':
    result = sum_of_nine_integers()
    print(result)