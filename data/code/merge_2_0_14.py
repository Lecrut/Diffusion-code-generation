def are_equal(a: object, b: object) -> bool:
    return a == b
if __name__ == '__main__':
    sample_list = [1, 'two', 3]
    sample_dict = {'key': 'value'}
    result_1 = are_equal(sample_list, [1, 'two', 3])
    print(f"List comparison: {result_1}")
    result_2 = are_equal(5.0, 5)
    print(f"Float vs Int comparison: {result_2}")
    result_3 = are_equal({'a': 1}, {'b': 1})
    print(f"Dict comparison (different keys): {result_3}")