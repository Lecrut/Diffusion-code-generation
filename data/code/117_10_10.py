def precise_difference(num1, num2):
    return round(num1 - num2, 4)

if __name__ == '__main__':
    number_one = 3.141592653589793
    number_two = 2.718281828459045
    result = precise_difference(number_one, number_two)
    print(result)