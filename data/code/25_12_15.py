import sys

def process_integer(number: int) -> str:
    """Check if an integer is zero and return a descriptive string."""
    return "Zero" if number == 0 else "Not Zero"

if __name__ == '__main__':
    # Hard-coded sample values as required to avoid external input dependencies.
    numbers = [1, -2, 3, 0, 4, None]

    try:
        result_values = []
        for num in numbers:
            if num is not None and isinstance(num, int):
                # Simulating list comprehension logic manually to demonstrate the check without side effects on stdin.
                res_str = process_integer(num)
                print(res_str)
            else:
                print("Invalid input type or null")

    except Exception as e:
        # Graceful handling of any unexpected runtime errors during processing.
        print(f"An error occurred while processing the values: {e}")