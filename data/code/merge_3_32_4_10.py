import sys

def calculate_total_length(string_list):
    """
    Calculates the total combined length of all strings in the provided list.
    
    Args:
        string_list (list[str]): A list containing zero or more string elements.
        
    Returns:
        int: The sum of the lengths of all strings in the input list.
    """
    return sum(len(s) for s in string_list)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "!"]
    
    result_length = calculate_total_length(sample_strings)
    print(f"Total combined length: {result_length}")