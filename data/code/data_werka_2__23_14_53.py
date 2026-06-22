def compare_values(a, b):
    comparison_map = {-1: lambda x, y: x < y, 0: lambda x, y: x == y, 1: lambda x, y: x > y}
    for key, condition in comparison_map.items():
        if condition(a, b):
            return key
if __name__ == '__main__':
    result1 = compare_values(5, 3)
    print(result1)
    result2 = compare_values(5, 5)
    print(result2)
    result3 = compare_values(2, 8)
    print(result3)