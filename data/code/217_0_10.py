def compare_integers(a, b):
    if a > b:
        return "greater than"
    elif a < b:
        return "less than"
    else:
        return "equal to"

if __name__ == '__main__':
    num1 = 20
    num2 = 30
    result = compare_integers(num1, num2)
    print(result)