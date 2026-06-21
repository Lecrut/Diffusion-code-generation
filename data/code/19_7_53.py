def is_condition_true(a, b):
    are_equal = (a == b)
    return are_equal

if __name__ == '__main__':
    first_sample_a = 100
    first_sample_b = 200
    first_result = is_condition_true(first_sample_a, first_sample_b)
    print(f"First comparison result: {first_result}")

    second_sample_a = "test"
    second_sample_b = "test"
    second_result = is_condition_true(second_sample_a, second_sample_b)
    print(f"Second comparison result: {second_result}")