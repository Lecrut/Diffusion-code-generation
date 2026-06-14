import sys
def compare_quantities(a_str, b_str):
    try:
        a = float(a_str)
        b = float(b_str)
        print(f"Quantity A: {a}")
        print(f"Quantity B: {b}")
        if a > b:
            print("Comparison Result: A is greater than B")
        elif a < b:
            print("Comparison Result: A is less than B")
        else:
            print("Comparison Result: A is equal to B")
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid numbers.")
if __name__ == '__main__':
    input_a = "15.7"
    input_b = "22.3"
    compare_quantities(input_a, input_b)