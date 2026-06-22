def compare_two_simple_quantities_now_transform(a, b):
    if a > b:
        return True
    elif b > a:
        return False
    else:
        return None

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_transform(5, 3)
    print(result)