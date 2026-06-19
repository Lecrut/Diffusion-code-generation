def are_identical(obj1, obj2):
    return obj1 is obj2

if __name__ == '__main__':
    sample_value_1 = 42
    sample_value_2 = 42
    result = are_identical(sample_value_1, sample_value_2)
    print(result)