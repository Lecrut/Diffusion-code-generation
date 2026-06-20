def sum_three_with_tuple(a, b, c):
    numbers = (a, b, c)
    return sum(numbers)

if __name__ == '__main__':
    num1, num2, num3 = 5, 10, 15
    result = sum_three_with_tuple(num1, num2, num3)
    print(result)