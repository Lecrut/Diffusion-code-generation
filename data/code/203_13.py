import sys
def compare_quantities(a_str, b_str):
    try:
        a = float(a_str)
        b = float(b_str)
        print("--- Comparison Results ---")
        print(f"Quantity A: {a}")
        print(f"Quantity B: {b}")
        if a > b:
            print("Result: Quantity A is greater than Quantity B.")
        elif a < b:
            print("Result: Quantity A is less than Quantity B.")
        else:
            print("Result: Quantity A is equal to Quantity B.")
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid numeric values.")
if __name__ == '__main__':
    input_a = "42.5"
    input_b = "100"
    compare_quantities(input_a, input_b)