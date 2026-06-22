def compare_two_simple_quantities_now_format_results(a: float, b: float) -> str:
    if a > b:
        return f"Number 1: {a}\nNumber 2: {b}\nThe larger number is {a} and the smaller number is {b}."
    else:
        return f"Number 1: {a}\nNumber 2: {b}\nThe larger number is {b} and the smaller number is {a}."

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_format_results(15.75, 8.25)
    print(result)