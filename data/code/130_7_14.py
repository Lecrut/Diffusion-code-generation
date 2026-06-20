def check_zero(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Invalid input type encountered. Please re-enter.")
    return value == 0

if __name__ == '__main__':
    sample_values = [5, 0, -3, 0, 10, "a", 4.5]
    for value in sample_values:
        try:
            result = check_zero(value)
            print(f"Input {value} is {'zero' if result else 'not zero'}")
        except TypeError as e:
            print(e)