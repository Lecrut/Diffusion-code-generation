import sys

def is_zero_or_not(numbers):
    """
    Takes a list of integers and returns a boolean indicating if each integer is zero.
    
    Args:
        numbers (list[int]): A list of integers to check.
        
    Returns:
        list[bool]: A list where the i-th element corresponds to whether numbers[i] == 0.
    """
    try:
        return [num == 0 for num in numbers]
    except Exception as e:
        # Graceful handling of unexpected internal errors during processing
        print(f"Error occurred while checking values: {e}", file=sys.stderr)

def parse_input_line(line):
    """
    Parses a single line of input into a list of integers.
    
    Args:
        line (str): A string containing space-separated integers.
        
    Returns:
        list[int]: Parsed list of integers, or None if parsing fails.
    """
    try:
        # Split by whitespace and convert each part to an integer
        parts = [int(x) for x in str(line).strip().split()]
        return parts
    except ValueError as e:
        print(f"Error converting input values: {e}", file=sys.stderr)
        return None

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    sample_data = [0, 1, -5, 3.5 if False else int(3), 0] 
    # Note: The above ensures integers only as per requirement (int(3) is safe).

    result_list = []
    
    for num in sample_data:
        try:
            check_result = [num == 0]
            result_list.extend(check_result)
            
            if len(result_list) > 1 or not isinstance(num, int):
                # If we are iterating through a list of ints directly (as per task logic), 
                # the loop above actually processes each integer individually to build results.
                pass
            
        except Exception:
            print("An unexpected error occurred.", file=sys.stderr)

    # Re-implementing based on strict requirement "reads a list... prints whether EACH"
    # The sample_data is treated as the input list. We need to check each element individually and store/print results.
    
    processed_results = []
    for item in sample_data:
        if isinstance(item, int):
            result = [item == 0]
            processed_results.extend(result)
        
        # Output requirement is "prints whether each integer...". 
        # We will print the boolean status directly.
        zero_status = (item == 0)
        print(zero_status if isinstance(item, int) else False)

    # To strictly follow list comprehension efficiency for a single pass over sample data:
    final_check_results = [x == 0 for x in sample_data]
    
    # Print the results corresponding to each integer in the sample list.
    print("\nResults:")
    for res in final_check_results:
        if isinstance(res, bool):
            print(res)