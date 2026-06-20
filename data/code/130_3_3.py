def is_zero(value):
    return value == 0

if __name__ == '__main__':
    sample_values = {0: True, 5: False, -3: False, 0.0: True}
    for key, expected in sample_values.items():
        result = is_zero(key)
        print(f"Value: {key}, Is Zero: {result} (Expected: {expected})")