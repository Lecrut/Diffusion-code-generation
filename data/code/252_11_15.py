def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    if a >= b:
        larger = f"{a:.2f}"
        smaller = f"{b:.2f}"
    else:
        larger = f"{b:.2f}"
        smaller = f"{a:.2f}"
    
    difference = abs(a - b)
    result_str = f"Larger: {larger}, Smaller: {smaller}, Difference: {difference:.2f}"
    return result_str

if __name__ == '__main__':
    num1 = 15.75
    num2 = 8.33
    print(compare_two_simple_quantities_now_format_results(num1, num2))