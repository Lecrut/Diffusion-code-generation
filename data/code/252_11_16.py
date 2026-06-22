def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    larger = max(a, b)
    smaller = min(a, b)
    difference = abs(a - b)
    
    result_str = f"Larger number: {larger}\nSmaller number: {smaller}\nDifference: {difference}"
    return result_str

if __name__ == '__main__':
    num1 = 15.75
    num2 = 8.25
    print(compare_two_simple_quantities_now_format_results(num1, num2))