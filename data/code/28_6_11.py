def compare_and_sort_numbers(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = compare_and_sort_numbers(42, 15)
    print(result)