def is_greater(a, b):
    return a > b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result = is_greater(num1, num2)
    print(f"{num1} is {'greater' if result else 'not greater'} than {num2}")