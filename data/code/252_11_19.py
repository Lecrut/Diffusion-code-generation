def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    if a >= b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    
    difference = abs(a - b)
    
    result = f"Number 1: {a}\n"
    result += f"Number 2: {b}\n"
    result += f"Larger number: {larger}\n"
    result += f"Smaller number: {smaller}\n"
    result += f"Difference: {difference}\n"
    
    return result

if __name__ == '__main__':
    num1 = 15.75
    num2 = 8.25
    formatted_result = compare_two_simple_quantities_now_format_results(num1, num2)
    print(formatted_result)