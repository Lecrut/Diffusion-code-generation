def compare_and_sort_numbers(a, b):
    if a < b:
        return (a, b)
    elif a > b:
        return (b, a)
    else:
        return (a, b)

if __name__ == '__main__':
    result = compare_and_sort_numbers(5, 3)
    print(result)