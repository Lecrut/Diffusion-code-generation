def are_booleans_equal(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    first_value = True
    second_value = False
    result = are_booleans_equal(first_value, second_value)
    print(result)