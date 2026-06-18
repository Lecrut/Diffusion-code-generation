import os

def read_volume_measurements(file_path):
    """
    Reads volume measurements from a file line by line, 
    converts each to float (handling trailing/leading whitespace),
    and returns the total sum along with any encountered errors.
    
    Args:
        file_path (str): Path to the file containing numbers
        
    Returns:
        tuple: (total_volume, error_message)
               If successful: (float(total), None)
               If failed due to IO or content issues: (0.0, str(error))
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            total = 0.0
            
            for line in f:
                cleaned_line = line.strip()
                
                # Skip empty lines or comments (lines starting with #)
                if not cleaned_line or cleaned_line.startswith('#'):
                    continue
                
                try:
                    value = float(cleaned_line)
                    total += value
                    
                except ValueError as ve:
                    raise RuntimeError(f"Invalid number format in line '{cleaned_line}': {ve}")

        return total, None
        
    except FileNotFoundError:
        error_msg = f"The file at path '{file_path}' was not found."
        return 0.0, error_msg

if __name__ == '__main__':
    pass
