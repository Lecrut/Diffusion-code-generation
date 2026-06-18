import re

def extract_valid_weights(weight_list: list) -> list:
    """
    Filters a list of weight measurements to return only valid, positive numbers.
    
    Args:
        weight_list (list): A list of strings representing weight measurements.
        
    Returns:
        list: A new list containing only the validated weights as floats or integers 
              if they are whole numbers. Negative values and non-numeric strings are excluded.
    """
    valid_weights = []
    
    for item in weight_list:
        try:
            # Check if string represents a number using regex to ensure format validity (optional digits, decimal point, optional sign)
            clean_value = re.sub(r'^\s*,?\s*', '', str(item).strip())
            
            # Attempt conversion first; this will raise ValueError or other exceptions for invalid types/formats
            try:
                numeric_value = float(clean_value)
                
                # Check if the string was effectively an integer representation without decimal part to return int
                is_whole_number = clean_value.replace('.', '').replace('-', '').isdigit() and '.' not in clean_value
                
                if valid_weight_check(numeric_value):
                    val_type = int if is_whole_number else float
                    valid_weights.append(val_type(numeric_value))
            except (ValueError, TypeError):
                # Catch cases where conversion fails due to non-numeric characters or format issues
                continue
                
        except Exception:
            # Gracefully handle any unexpected errors during processing of a single item
            continue
            
    return valid_weights

def valid_weight_check(weight_value) -> bool:
    """Helper function to validate if the weight value is positive."""
    try:
        val = float(weight_value)
        return val > 0
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    # Sample data with potential valid integers and floats, invalid negatives, non-numbers, and mixed types
    sample_data = ["5.5 kg", "10kg", "-3 lbs", "abc", "", "$20", 7, "98"]

    processed_weights = extract_valid_weights(sample_data)
    
    print("Valid weights:", processed_weights)