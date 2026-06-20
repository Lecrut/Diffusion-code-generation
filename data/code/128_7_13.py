def check_negative(value):
    if value < 0:
        raise ValueError("Negative value detected")

if __name__ == '__main__':
    sample_values = [-1, 0, 1]
    for val in sample_values:
        try:
            check_negative(val)
            print(f"Value {val} is not negative.")
        except ValueError as e:
            print(e)