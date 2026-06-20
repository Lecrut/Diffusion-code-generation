def negate_boolean(value):
    return not value

if __name__ == '__main__':
    samples = {True: False, False: True}
    for sample, expected in samples.items():
        result = negate_boolean(sample)
        print(f"Input: {sample}, Output: {result}")