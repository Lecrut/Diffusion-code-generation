def compare_values(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a > b

if __name__ == '__main__':
    try:
        result1 = compare_values(25, 20)
        print(f"25 is greater than 20: {result1}")

        result2 = compare_values(10, 15)
        print(f"10 is greater than 15: {result2}")

        result3 = compare_values(7, 7)
        print(f"7 is greater than 7: {result3}")
    except ValueError as e:
        print(e)