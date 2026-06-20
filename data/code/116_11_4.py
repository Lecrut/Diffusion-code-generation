def sum_of_values(a, b, c):
    return a + b + c

if __name__ == '__main__':
    constants = {'num1': 10, 'num2': 25, 'num3': 40}
    result = sum_of_values(constants['num1'], constants['num2'], constants['num3'])
    print(result)