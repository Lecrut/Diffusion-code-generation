MIDDLE_INDEX = 1

def find_the_middle_value_among_three_calculate(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[MIDDLE_INDEX]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_calculate(3, 2, 1))
    print(find_the_middle_value_among_three_calculate(4, 6, 5))
    print(find_the_middle_value_among_three_calculate(7, 8, 9))
    print(find_the_middle_value_among_three_calculate(-3, -2, -1))
    print(find_the_middle_value_among_three_calculate(0, 0, 0))