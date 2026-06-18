import sys

def check_integers(int_list):
    """
    Takes a list of integers and returns a boolean indicating whether each integer is zero.
    
    Parameters:
        int_list (list[int]): List of integers to evaluate
        
    Returns:
        list[bool]: A corresponding list where True represents non-zero values, 
                   False represents zero values
    """
    return [x != 0 for x in int_list]

def parse_integers_from_string(input_str):
    """
    Parses a string of comma-separated integers into a list.
    
    Parameters:
        input_str (str): String containing space or comma separated integers
        
    Returns:
        list[int]: List of parsed integers, empty if parsing fails due to non-integer content
                   Note: This function assumes the entire string is valid for integer conversion 
                   unless an exception occurs during processing. In this context, we catch errors gracefully.
    """
    try:
        # Split by comma or space and filter out any empty strings resulting from splitting
        parts = [part.strip() for part in input_str.split(',') + ['']]  # Ensure split handles trailing commas/spaces cleanly if needed
        
        int_list = []
        valid_count = 0
        total_parts = len(parts) - (1 if '' in parts else 0)

        for p in parts:
            try:
                val = int(p)
                int_list.append(val)
                valid_count += 1
            except ValueError:
                # Gracefully skip non-integer tokens or malformed numbers by stopping here 
                # to avoid crashing the whole script, though strict validation might require explicit error handling.
                break
        
        return int_list if len(int_list) > 0 else []
    except Exception as e:
        print(f"Error parsing input string: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    sample_input_str = "0, 5, -3, , 2"
    
    try:
        int_list = parse_integers_from_string(sample_input_str)
        
        if not isinstance(int_list, list):
            print("Error: Input parsing failed to produce a valid integer list.", file=sys.stderr)
            sys.exit(1)

        result_flags = check_integers(int_list)
        for i, is_non_zero in enumerate(result_flags):
            val = int_list[i] if i < len(int_list) else None
            status_str = "Zero" if not is_non_zero else "Non-Zero"
            
            # Print the value and its corresponding zero check result
            print(f"{val} -> {status_str}")

    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)