def are_values_equal(value1: any, value2: any) -> bool:
    return value1 == value2
if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(5, '5'))