def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample_values = {True: True, False: False}
    result = compare_booleans(sample_values[True], sample_values[False])
    print(result)