def are_values_equal(a: any, b: any) -> bool:
    return a == b
if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(5, '5'))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal([1, 2], [2, 1]))