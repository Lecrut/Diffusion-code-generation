def validate_properties(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a numeric type")
    
    is_positive = value > 0
    is_even = value % 2 == 0
    is_small = value < 100
    
    positive_status = "positive" if is_positive else "not positive"
    even_status = "even" if is_even else "odd"
    size_status = "less than 100" if is_small else "100 or greater"
    
    if is_positive and is_even and is_small:
        return f"{value} is {positive_status}, {even_status}, and {size_status}"
    
    failures = []
    if not is_positive:
        failures.append("not positive")
    if not is_even:
        failures.append("not even")
    if not is_small:
        failures.append("not less than 100")
        
    return f"{value} is {', '.join(failures)}"

if __name__ == '__main__':
    test_inputs = [24, 75, -3, 100, 99.5]
    for num in test_inputs:
        output = validate_properties(num)
        print(output)