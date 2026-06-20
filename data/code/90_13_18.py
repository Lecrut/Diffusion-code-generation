def check_or_condition(a, b):
    return bool(int(a) | int(b))

if __name__ == '__main__':
    sample_a = "1"
    sample_b = "0"
    result = check_or_condition(sample_a, sample_b)
    print(result)