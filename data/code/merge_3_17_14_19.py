def check_parity(number: int) -> str:
    """Check if a number is even or odd."""
    return "The entered number is EVEN." if number % 2 == 0 else "The entered number is ODD."

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    test_values = [4, -3, 17]

    for val in test_values:
        try:
            result_message = check_parity(val)
            print(f"Input: {val} -> {result_message}")
        except Exception as e:
            # This block is technically unreachable with integer inputs but demonstrates structure.
            print(f"Error processing input {val}: {e}", file=__import__('sys').stderr)

    # Additional test for non-integer simulation to demonstrate error handling logic if the number wasn't valid type (though passed as int here).
    try:
        invalid_input = "123abc"  # Simulating a scenario where input might not be an integer.
        check_parity(invalid_input)
    except TypeError:
        print("Error Handling Active: Non-integer input detected and handled gracefully.")