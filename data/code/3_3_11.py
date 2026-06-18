import sys

def parse_and_convert(line):
    """
    Parses a line containing temperature and unit (e.g., '30 C'),
    converts to Kelvin, and returns the result as a string.
    If parsing fails or conversion is invalid, it prints an error message
    but does not exit the program.
    
    Args:
        line (str): Input string with format "value unit" where unit is 'C' or 'F'.
        
    Returns:
        str: Temperature in Kelvin formatted to two decimal places.
    """
    try:
        parts = line.strip().split()
        if len(parts) < 2:
            return None
        
        temp_str, unit_str = parts[0], parts[-1]
        
        # Normalize unit string (case-insensitive check for C or F)
        unit_upper = unit_str.upper()
        if unit_upper not in ('C', 'F'):
            print(f"Error: Unsupported temperature unit '{unit_str}'. Expected 'C' or 'F'.")
            return None
        
        value = float(temp_str)
        
        # Convert to Kelvin based on input unit
        if unit_upper == 'C':
            kelvin_value = value + 273.15
        elif unit_upper == 'F':
            kelvin_value = (value - 32) * 5 / 9 + 273.15
        
        return f"{kelvin_value:.2f} K"
    
    except ValueError:
        print(f"Error: Invalid temperature value '{temp_str}'.")
        return None

def main():
    """
    Main execution block that processes standard input line by line,
    converts temperatures to Kelvin, and prints the results.
    Includes a sample test case when run directly as __main__.
    
    Constraints:
        - No user interaction via input() or sys.stdin.read().
        - Simulated data processing for demonstration if no stdin is provided in testing environments that support it (though per task constraints, we rely on the hardcoded block).
        
    Note: Since the task forbids calling input(), sys.stdin directly for reading, 
    and requires a runnable module with hard-coded samples, this function will simulate 
    standard behavior by processing data from stdin if available in an actual run. 
    However, to strictly adhere to "Never call ... sys.stdin" while providing runnable code:
    
    The script is designed to read from stdin normally. For the `if __name__ == '__main__':` block,
    we will simulate a few lines of input directly into memory since external interaction or files 
    are prohibited during this specific execution context simulation. In a real environment where 
    standard input IS available (as per typical script usage), it would read from sys.stdin line by line.
    
    To balance the requirement "Never call ... sys.stdin" with providing runnable code that works:
    We will implement the reading logic to use `sys.stdin` because Python scripts MUST interact with stdin 
    if they are meant to be run as command-line tools processing input, unless data is hardcoded in a loop.
    
    Re-reading constraints carefully: "Never call ... sys.stdin". This implies we cannot read from it at all?
    But the task says "reads temperature data from standard input". These two seem contradictory if interpreted strictly 
    without stdin access. 
    
    Interpretation for this specific constraint set ("Return only a single complete runnable Python module" + "No sys.stdin"):
    The script should be capable of running with hardcoded samples in the main block to satisfy execution requirements, 
    while defining the logic to handle standard input if it were available (for completeness), but strictly avoiding 
    explicit calls like `sys.stdin.readline()` or `input()`. 
    
    However, a Python module that "reads from standard input" must interact with stdin. If I cannot call sys.stdin, 
    how can it read? The only way is to rely on the hardcoded block for demonstration purposes in this specific constrained environment,
    OR assume the user will pipe data in (which requires `sys.stdin` or `input()`). 
    
    Given the strict prohibition "Never call input(), sys.stdin...", I must simulate the reading process using 
    a list of strings defined locally to represent stdin content. This satisfies "reads ... from standard input" logically 
    by processing the provided dataset, and avoids illegal function calls while being runnable without external files or args.
    
    Thus: The `main` block will define local variables representing the input stream lines.
    """
    
    # Simulated Standard Input Data (Hardcoded)
    simulated_stdin_lines = [
        "30 C",
        "-45 F",
        "100 K"  # Already in Kelvin, logic handles it if we extended support, but task only asks for C/F conversion usually. 
               # Let's stick to converting C and F as per typical needs unless specified otherwise. 
               # The prompt says "extract the temperature and unit... converted ... in Kelvin".
               # If input is already K, our current logic might fail or need extension. 
               # To be safe and robust: extend conversion logic for 'K' to just output it (or handle gracefully).
    ]
    
    extended_unit_check = True
    
    def parse_and_convert_extended(line):
        try:
            parts = line.strip().split()
            if len(parts) < 2:
                return None
            
            temp_str, unit_str = parts[0], parts[-1]
            
            # Normalize unit
            unit_upper = unit_str.upper()
            
            value = float(temp_str)
            
            # Conversion logic covering C and F. If K is provided, we assume it's already Kelvin or treat as error? 
            # Usually tasks imply converting FROM Celsius/Fahrenheit TO Kelvin. 
            # Let's handle 'K' input by returning the same value to be safe.
            if unit_upper == 'C':
                kelvin_value = value + 273.15
            elif unit_upper == 'F':
                kelvin_value = (value - 32) * 5 / 9 + 273.15
            elif unit_upper == 'K':
                kelvin_value = float(temp_str) # Already Kelvin, or potentially a typo in input if they meant C? 
                                               # Assuming valid K means return as is.
            
            return f"{kelvin_value:.2f} K"
        except ValueError:
            print(f"Error: Invalid temperature value '{temp_str}'.")
            return None

    lines = simulated_stdin_lines
    
    for line in lines:
        result = parse_and_convert_extended(line)
        if result is not None:
            print(result)

if __name__ == '__main__':
    main()