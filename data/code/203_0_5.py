def compare_numbers(a, b):
    if a > b:
        return 'Greater'
    elif a < b:
        return 'Lesser'
    else:
        return 'Equal'

if __name__ == '__main__':
    result = compare_numbers(10, 5)
    print(result)