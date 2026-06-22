def compare_integers(a, b):
    if a > b:
        return "greater than"
    elif a < b:
        return "less than"
    else:
        return "equal to"

if __name__ == '__main__':
    result = compare_integers(8, 3)
    print(result)