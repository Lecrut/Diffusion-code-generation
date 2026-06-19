def is_condition_true(a, b):
    try:
        return a == b
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result = is_condition_true(sample_a, sample_b)
    print(result)