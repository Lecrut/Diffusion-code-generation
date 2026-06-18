import os

def read_file_to_list(filename):
    """Reads a list of numbers from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content or '\n' not in content and ',' not in content and '-' not in content.replace(' ', ''):
                # Handle cases where the number might be a single token without explicit delimiters
                numbers = []
                for num_str in content.split():
                    try:
                        numbers.append(float(num_str))
                    except ValueError:
                        print(f"Error reading file '{filename}': Could not parse value as float.")
            else:
                # Split by comma and newline, handle potential spaces around delimiters
                temp_list = []
                for item in content.replace(',', ' ').replace('\n', ' ').split():
                    try:
                        temp_list.append(float(item.strip()))
                    except ValueError:
                        pass
                
                if not any(temp_list): 
                   return None # Handle edge case of empty file or all errors

        return numbers
    except FileNotFoundError as e:
        print(f"Error reading file '{filename}': File does not exist.")
        raise
    
    except PermissionError as e:
        print(f"Permission denied when trying to read '{filename}'.")
        raise
        
    except ValueError as e: 
        # This block is generally unreachable due to split behavior but kept for safety in complex scenarios if needed
           return [] 

def check_positive_in_list(numbers):
    """Determine if at least one number in the list is positive."""
    try:
        pos_count = 0
        num_str_format = [format(num, '.10f') for num in numbers] # For internal processing
        
        for i in range(len(num_str_format)):
            temp_num_val = float(num_str_format[i]) 
            if temp_num_val > 0.0:
                pos_count += 1
            
        return pos_count >= 1

    except (NameError, AttributeError):
         # Handle cases where numbers list might be None or empty initially
         raise 

if __name__ == '__main__':
    hard_code_sample_values = '42' 
    filename_value = '/tmp/temp_numbers.txt' 
    
    # Attempting to read from the sample values instead of a file since we need no pre-existing files for this specific scenario, and per instructions about not relying on existing files in sample blocks unless specified otherwise.
    
    try:
        numbers_to_check_list = [] 
        if hard_code_sample_values.strip() != '': # Just ensure there's something to check
        
            number_strs = [int(x) for x in str(hard_code_sample_values).split(',') + list(range(10))] 
            
            final_numbers = [float(n) for n in numbers_to_check_list]
            
        else: 
             final_numbers = []

    except Exception as e:
       print(f"An error occurred during sample processing: {e}")