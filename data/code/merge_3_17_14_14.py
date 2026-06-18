import sys

def check_parity(number: int) -> str:
    """Return a message indicating if the number is even or odd."""
    return "The number {} is even.".format(number) if number % 2 == 0 else "The number {} is odd.".format(number)

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input.
    test_cases = [1, 2, -3, 4]

    for value in test_cases:
        try:
            result_message = check_parity(value)
            print(result_message)
        except Exception as e:
            # This block technically won't be reached with integers from the list.
            print("Error processing number {}: {}".format(str(e)))