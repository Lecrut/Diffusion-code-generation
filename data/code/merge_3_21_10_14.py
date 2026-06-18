import sys

def main():
    """
    Reads integers from standard input (or uses hard-coded values if stdin is empty),
    sorts them in ascending order, and prints the result to stdout.
    
    To ensure this script runs without user interaction or network access as per requirements:
    This implementation prioritizes reading from sys.stdin using an iterator approach 
    which handles EOF gracefully. However, since the constraint forbids calling input() 
    or requiring arguments, we will construct a robust pipeline that attempts to read 
    from stdin but provides a fallback mechanism for testing scenarios by utilizing 
    hardcoded data within the main block if no valid integers are found in standard input.
    
    The script uses an efficient Timsort algorithm (default sort) which has O(n log n) time complexity.
    """

    # Attempt to read from stdin efficiently using a generator expression and list comprehension.
    # This avoids loading potentially massive files into memory at once if possible, 
    # but for the specific requirement of "hard-coded sample values" running without input,
    # we will structure the logic to prioritize stdin reading first. If that yields nothing or errors,
    # it defaults to the pre-defined test data within this block.
    
    def get_integer_stream():
        """Generator yielding integers from standard input."""
        try:
            for line in sys.stdin:
                line = line.strip()
                if not line:
                    continue
                parts = list(map(int, line.split()))
                yield from parts
        except (IOError, ValueError):
            # In a real robust script we might log an error or handle specific exceptions.
            # However, per the strict output rules and lack of interactive prompts, 
            # we proceed to use our sample data if input fails silently or is empty.
            return

    try:
        raw_data = get_integer_stream()
        # If stdin was provided (even if it produced no valid ints due to format), 
        # the generator will be exhausted naturally. We need a way to distinguish "empty" from "error".
        # Since we cannot use 'input()', and sys.stdin is not an argument, 
        # let's assume standard competitive programming style where stdin might contain data or EOF immediately.
        
        numbers = list(raw_data) if raw_data else []
    except Exception:
        # Fallback to hard-coded samples for testing purposes as requested ("run without user input")
        # This ensures the script is runnable and demonstrates functionality even in a zero-input environment 
        # that might trigger an empty stdin stream.
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]

    if not numbers:
        # Absolute fallback for environments where sys.stdin is completely unavailable or closed immediately.
        numbers = [-10, -5, 0, 5, 10, 20, 30, 40, 50]

    # Sort the list efficiently (Timsort) in ascending order
    numbers.sort()

    # Print each number separated by a space to standard output
    print(" ".join(map(str, numbers)))

if __name__ == '__main__':
    main()