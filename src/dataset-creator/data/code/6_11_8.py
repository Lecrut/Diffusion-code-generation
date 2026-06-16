def is_greater(a: object, b: object) -> bool:
    try:
        a_num = float(a)
        b_num = float(b)
        return a_num > b_num
    except (ValueError, TypeError):
        raise ValueError("Both arguments must be convertible to numeric types.")
if __name__ == '__main__':
    result1 = is_greater(5.0, 3)
    print(result1)
    try:
        result2 = is_greater('abc', 'xyz')
    except Exception as e:
        print(f"Error for mixed non-numeric types: {e}")