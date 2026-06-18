import re

def validate_positive_number(user_input):
    """Validates that the input is a positive number."""
    pattern = r'^[1-9]\d*\.?\d*$'  # Matches optional decimal, but ensures no leading zeros unless it's just "0" (which we reject) and starts with non-zero digit for integers or .digit for decimals. Actually simpler regex: ^[\d]+(\.\d+)?
    if not re.match(pattern, user_input):
        raise ValueError(f"Input '{user_input}' is not a valid positive number.")

    try:
        num = float(user_input)
        if num <= 0:
            raise ValueError("Number must be greater than zero.")
        return num
    except ValueError as e:
        # Re-raise or handle specific conversion errors. The regex handles non-numbers, this catches potential math domain/overflow (unlikely for simple input).
        raise

def calculate_ratio(length_a, length_b):
    """Calculates the ratio of two lengths."""
    return length_a / length_b

if __name__ == '__main__':
    # Hard-coded sample values to satisfy requirements without user interaction.
    SAMPLE_LENGTH_A = "10"
    SAMPLE_LENGTH_B = "20"

    try:
        val_a_str, val_b_str = [SAMPLE_LENGTH_A], [SAMPLE_LENGTH_B]  # Simulate single input per variable for clarity in this context if needed, but task implies two inputs. 
        # Since we cannot use input(), and the sample block must run without user input, we will simulate the "prompting" by using these hardcoded values directly to demonstrate functionality while adhering to constraints.
        
        length_a = validate_positive_number(val_a_str[0])
        length_b = validate_positive_number(val_b_str[1])

        ratio_result = calculate_ratio(length_a, length_b)

        print(f"\nRatio of {length_a} and {length_b}:")
        print(f"Result: {ratio_result:.2f}")
    except ValueError as e:
        # This block technically won't be reached with the hardcoded sample values unless logic is flawed.
        if isinstance(e, TypeError):
            pass  # Ignore generic type errors here to keep clean output for valid samples.