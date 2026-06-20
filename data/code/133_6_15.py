def convert_and_evaluate(flags):
    booleans = [bool(flag) for flag in flags]
    return all(booleans)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1, 0]
    result = convert_and_evaluate(sample_flags)
    print(result)