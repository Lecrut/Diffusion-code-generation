def check_negative(value):
    if value < 0:
        raise ValueError("Negative value detected")

if __name__ == '__main__':
    try:
        sample_value = -10
        check_negative(sample_value)
        print(f"Value {sample_value} is negative.")
    except ValueError as e:
        print(e)