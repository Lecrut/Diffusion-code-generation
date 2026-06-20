def check_zero(value):
    if isinstance(value, (int, float)) and value == 0:
        return True
    else:
        raise ValueError("Input must be exactly zero")

if __name__ == '__main__':
    sample_values = [5, 0, -3, 0, 10, "a", 4.5]
    for val in sample_values:
        try:
            result = check_zero(val)
            print(f"Input {val} is {'zero' if result else 'not zero'}")
        except ValueError as e:
            print(e)