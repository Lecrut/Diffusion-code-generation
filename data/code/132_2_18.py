def check_condition(n):
    return n > 0 and not (n & 1)

if __name__ == '__main__':
    sample_values = [5, -3, 0, 2]
    for value in sample_values:
        result = check_condition(value)
        print(f"check_condition({value}): {result}")