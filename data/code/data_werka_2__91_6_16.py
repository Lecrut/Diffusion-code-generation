def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        result = negate_boolean(val)
        print(result)