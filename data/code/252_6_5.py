def compare_two_simple_quantities_now_convert_all(quantity1, quantity2):
    if not isinstance(quantity1, (int, float)) or not isinstance(quantity2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    return quantity1 + quantity2

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_convert_all(5, 3)
    print(result)