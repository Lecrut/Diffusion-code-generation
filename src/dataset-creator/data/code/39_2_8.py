def find_largest_element(lst):
    for idx, item in enumerate(lst):
        if not isinstance(item, (int, float)):
            raise TypeError(f"Invalid data type at index {idx}: expected int or float, got {type(item).__name__}")
    max_val = lst[0]
    for val in lst:
        try:
            num1 = float(max_val)
            num2 = float(val)
            if num2 > num1:
                max_val = num2
        except (ValueError, OverflowError):
            raise ValueError(f"Cannot compare values due to unsupported numeric conversion")
    return int(max_val)
if __name__ == '__main__':
    data = [3.5, 7, "not a number", -10]
    try:
        result = find_largest_element(data)
        print(f"Largest element is {result}")
    except (TypeError, ValueError) as e:
        print(f"Error encountered: {e}")