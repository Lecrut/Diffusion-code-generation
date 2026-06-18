def is_greater(a: any, b: any) -> bool:
    try:
        a_num = float(a)
        b_num = float(b)
        return a_num > b_num
    except (ValueError, TypeError):
        raise ValueError("Both arguments must be convertible to numbers.")
if __name__ == '__main__':
    result = is_greater(10.5, 7)
    print(result)