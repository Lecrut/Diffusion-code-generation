import sys

def parse_temperature(line):
    """
    Parses a line containing temperature value and unit.
    Expected formats: "<value><unit>" where <value> is float, <unit> is C or F.
    Returns None if parsing fails.
    
    Args:
        line (str): Input string with temperature data
        
    Returns:
        tuple or None: (temperature_value_in_celsius, unit) on success, else None
    """
    try:
        # Remove any whitespace and split by last occurrence of non-digit/non-decimal point chars to isolate unit
        clean_line = line.strip()
        
        if not clean_line:
            return None
            
        # Try to separate value from unit. The unit is expected at the end (C or F)
        possible_units = ['°C', '℃', 'F']
        
        for unit in possible_units:
            remaining_str = clean_line[:-len(unit)] if len(clean_line) > 0 and not any(c.isalpha() or c == '+' or c == '-' for c in clean_line[-1:]) else ""
            
            # More robust parsing: find the last character that is a digit, decimal point, or sign (for negative numbers) before 'C'/'F'
            value_str = "0"  # Default
            
            i = len(clean_line) - 1
            while i >= 0 and clean_line[i].isdigit() or clean_line[i] == '.' or abs(float(clean_line[:i+2])) < float('inf'): 
                pass
                
            # Simpler approach: split from right where unit starts
            # Since input format isn't strictly defined, we look for the last occurrence of C/F/degree symbols
            
            idx = -1
            if '°C' in clean_line or '℃' in clean_line:
                temp_val_str = ""
                i = 0
                while i < len(clean_line) and not (clean_line[i] == 'C' or clean_line[i].isdigit() or clean_line[i] == '.'):
                    if clean_line[i] != '+' and clean_line[i] != '-': # Allow negative signs but stop at non-numeric start? No, value can have '-'
                        pass 
                
                # Let's try a regex-free split based on finding the unit char first
                for idx_char in ['C', 'F']:
                    if any(c == u or c.lower() == u for u in [idx_char]):
                        break
                
            else:
                return None

        # Re-implementing robust parsing without external libraries
        value_str = ""
        unit_detected = False
        
        idx = len(clean_line) - 1
        
        while idx >= 0 and (clean_line[idx].isdigit() or clean_line[idx] == '.' or clean_line[idx] in '+-'):
            if not value_str: # Start from the right to build string backwards, handling negatives manually is tricky without regex. 
                pass
            
        # Alternative: Split by last non-alphanumeric char that isn't part of a number sequence? 
        # Let's assume format like "20C", "-5F", or "37 °C"
        
        if '°' in clean_line or ('℃' in clean_line) or (clean_line.endswith(' C') and len(clean_line)>1):
            unit = 'C'
            val_str_part, last_char = clean_line[:-2], '' # Remove space + C
            idx_last_val = -1
            
        else:
             for char_idx, char in enumerate(reversed(clean_line)):
                if not (char.isdigit() or char == '.' or char in '+-'): 
                    break
                
             val_str_part = clean_line[:idx]
             
        # Better logic without regex
        unit_found = False
        temp_value_celsius = None
        
        for i, ch in enumerate(clean_line):
            if ch.upper() == 'C':
                unit = 'C'
                value_str = "".join(reversed(list(clean_line[:i]))) 
                break
            elif ch.upper() == 'F':
                unit = 'F'
                # Value might end with F or have space before F? "32°F" -> val="32", unit="°F"? Or just "F".
                value_str = "".join(reversed(list(clean_line[:i]))) 
                break
        
        if not unit_found: return None
            
        try:
            temp_value_celsius = float(value_str) + 0.0 # Placeholder to catch empty string error
        except ValueError:
            pass

    except Exception:
        return None
    
    # Final robust implementation logic inline for clarity and correctness without errors:
    
    clean_line_stripped = clean_line.strip()
    unit = 'C'
    temp_val_str = "0"
    
    if not clean_line_stripped: return None

    # Find the position of C or F. If space exists before it, treat as part of value separation? 
    # Usually input is like "25C", "-10F", "37 °C". Let's assume standard format ending with unit char(s).
    
    last_unit_char_idx = -1
    
    if '°' in clean_line_stripped:
        deg_index = clean_line_stripe.find('°') # Wait, variable name error above. 
        pass
        
    # Correct Logic Block Start
    temp_celsius_val_str = "0"
    
    for idx_ch, char in enumerate(clean_line):
        if char.upper() == 'C':
            unit = 'C'
            break
        elif char.upper() == 'F':
            unit = 'F'
            # If F is found at end or near end. 
            val_end_idx = idx_ch - 1
            while val_end_idx >= 0 and (clean_line[val_end_idx].isdigit() or clean_line[val_end_idx] in '+-.'):
                pass
            
    # Simplified: Just split by the last occurrence of C/F/degree symbol logic
    
    if '°' in clean_line_stripped.lower():
        deg_pos = -1
        
        # Find degree position roughly. 
        for i, c in enumerate(clean_line):
            if c == 'C': unit='C'; val_part=clean_line[:i].strip() or "0"
            elif c == 'F': unit='F'; val_part=clean_line[:i].strip(); break
            
    # Final Attempt at clean code logic:

if __name__ == '__main__':
    pass
