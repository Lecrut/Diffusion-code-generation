def compare_values(a, b):
    if a > b:
        return 'Greater'
    elif a < b:
        return 'Lesser'
    else:
        return 'Equal'

if __name__ == '__main__':
    num1 = 42
    num2 = 24
    result = compare_values(num1, num2)
    print(result)