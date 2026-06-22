MAX_VALUE = 100

def compare_two_simple_quantities_now_transform(a, b):
    return a > b if a <= MAX_VALUE and b <= MAX_VALUE else None

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_transform(5, 3)
    print(result)