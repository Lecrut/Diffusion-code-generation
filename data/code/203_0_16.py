def compare_numbers(a, b):
    if a > b:
        return 'Greater'
    elif a < b:
        return 'Lesser'
    else:
        return 'Equal'

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    result = compare_numbers(num1, num2)
    print(result)