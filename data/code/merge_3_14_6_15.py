def validate_numeric(value):
    """Check if a string is numeric."""
    try:
        float(value)
        return True, None
    except (ValueError, TypeError):
        return False, f"Invalid number type or format for {value}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    measurement_a = 123450
    measurement_b = 67890

    try:
        val_a, error_msg_a = validate_numeric(measurement_a)
        
        if not val_a or (error_msg_a is not None):
            print(f"Error comparing measurements A: {error_msg_a}")
            exit(1)

        try:
            val_b, error_msg_b = validate_numeric(str(measurement_b))

            if not val_b or (error_msg_b is not None):
                print(f"Error comparing measurements B: {error_msg_b}")
                exit(1)

            a_float = float(val_a)
            b_float = float(val_b)

            if a_float < b_float:
                result = "A < B"
            elif a_float > b_float:
                result = "A > B"
            else:
                result = f"A == {a_float}"
            
            print(result)

        except Exception as e:
            # Fallback for any unexpected calculation errors (e.g., overflow/underflow in some contexts).
            if val_a and val_b is not None:
                try:
                    a_val, b_val = float(val_a), float(str(measurement_b))
                    print(f"Conversion to number failed or invalid comparison logic")
                except ValueError:
                    print("Error comparing measurements B could not be converted.")
            else:
                print("An unexpected error occurred during the calculation process:")
    except Exception as e:
        # Final safety net for any parsing issues.
        print(f"Unexpected execution failure: {e}")