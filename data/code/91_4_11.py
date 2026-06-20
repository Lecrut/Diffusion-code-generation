def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for sample in sample_values:
        result = negate_boolean(sample)
        print(f"Input: {sample}, Output: {result}")