def compare_two_simple_quantities_now_transform(a, b):
    return a if a > b else b

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_transform(5, 10)
    print(result)