def convert_and_evaluate(flags):
    bool_flags = [bool(flag) for flag in flags]
    return all(bool_flags)

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1]
    print(convert_and_evaluate(sample_flags))