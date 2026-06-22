def logical_not(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        result = logical_not(val)
        print(result)