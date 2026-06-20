def are_values_equal(a: any, b: any) -> bool:
    return a == b
if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal('hello', 'hello'))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal(10, '10'))