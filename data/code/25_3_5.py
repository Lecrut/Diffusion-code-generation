try:
    value = 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

if __name__ == '__main__':
    sample_values = [
        42,
        -5,
        3.7,      # Non-integer to test handling (may raise ValueError if not handled specifically below)
        "abc"     # String input simulation via exception or direct check
    ]

    for val in sample_values:
        try:
            int_val = int(val)
            print(f"The value {val} converted to integer is {int_val}.")
            print("The entered number is zero:", end=" ")
            
            if int_val == 0:
                print("It IS zero.")
            else:
                print("It is NOT zero.")
        except ValueError as ve:
            # Handles cases where input cannot be converted to an integer (e.g., float like 3.7 or string "abc")
            if isinstance(val, float):
                print(f"The value {val} has a fractional part and cannot represent whole number exactly without rounding.")
            else:
                print(f"Input '{val}' is not valid numeric data for integer comparison.")
        except Exception as ex:
            # Fallback for unexpected errors during processing specific sample types if any occur
            print(f"Error while validating input {type(val).__name__}: {ex}")