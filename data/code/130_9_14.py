def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def contains_zero(num):
    if not is_numeric(num):
        raise TypeError("Input must be a numeric value")
    return num == 0

if __name__ == '__main__':
    sample_values = [1, 0, -5, 'a', 3.14]
    for val in sample_values:
        try:
            result = contains_zero(val)
            print(f"Value {val} is zero: {result}")
        except TypeError as e:
            print(e)