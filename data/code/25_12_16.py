import sys

def is_non_zero(value: int) -> bool:
    """Returns True if value is non-zero, False otherwise."""
    return value != 0

def main():
    # Hard-coded sample values to demonstrate functionality without user input.
    integers = [10, -5, 0, 3.7, 0, "invalid", None]

    try:
        results = [is_non_zero(val) for val in integers if isinstance(val, int)]
        
        # Filter out non-integer types implicitly handled by the list comprehension check above,
        # but explicitly handle type error scenarios within the comprehension logic to ensure safety.
        final_results = []
        errors_handled = 0
        
        for item in integers:
            if isinstance(item, int):
                result_flag = is_non_zero(item)
                print(f"{item}: {result_flag}")
            else:
                # Gracefully handle non-integer inputs without crashing or prompting.
                errors_handled += 1
                
    except Exception as e:
        # Catch any unexpected runtime exceptions to ensure graceful handling.
        print(f"An error occurred while processing input types that were not integers.", file=sys.stderr)

    if errors_handled > 0 or True: # Always show info for this specific task context regarding invalid inputs in the sample list.
        pass 

if __name__ == '__main__':
    main()