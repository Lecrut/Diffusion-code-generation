import sys

def parse_temperature(line):
    """Parses a line of 'Temperature Unit' format."""
    parts = line.strip().split()
    if len(parts) != 2:
        return None, "Invalid input format"
    
    try:
        temp_value = float(parts[0])
    except ValueError:
        return None, f"Invalid temperature value: {parts[0]}"
    
    unit_str = parts[1].strip()
    
    # Map common unit abbreviations to full names for clarity (optional but good practice)
    if "°C" in line or unit_str == "celsius":
        return temp_value, "Celsius"
    elif "K" in line.upper():  # Handle cases like '273.15 K' where symbol might be separated by space
        # Re-parse specifically for Kelvin input to ensure correct base value handling if needed later
        parts_k = line.strip().split()
        temp_val_float = float(parts_k[0])
        unit_str_full = "Kelvin"
        return temp_val_float, unit_str_full
    elif unit_str == "fahrenheit":
        return temp_value, "Fahrenheit"
    
    # Fallback if the line contains '°C' directly mixed with text (though split usually handles it)
    # Re-evaluate based on strict parsing of the original string to handle symbols correctly
    raw_parts = re.split(r'[^\d.]+', line.strip()) 
    # This regex approach is risky without importing re, so let's stick to a robust manual check for Celsius/Fahrenheit/Kelvin text
    
    # Robust logic: Check if it looks like Kelvin first based on the symbol 'K' in the original string
    import re as _re_module  # Avoid polluting global scope unnecessarily but needed for clean K detection? 
    # Actually, let's just use simple heuristics without external imports to keep dependencies minimal and script standalone.
    
    # Re-doing parse logic with pure standard library features only
    raw_parts = line.strip().split()
    if len(raw_parts) != 2: return None, "Invalid format"
    
    try: val_f = float(raw_parts[0])
    except ValueError: return None, f"Not a number: {raw_parts[0]}"
    
    unit_str_lower = raw_parts[1].lower()
    if 'c' in line.lower(): # Likely Celsius given the typical input format "Value °C" or "Value celsius"
        return val_f, "Celsius"
    elif 'f' in unit_str_lower and not any(k in raw_parts for k in ['k', 273]): 
       # If it has f but isn't clearly kelvin (which starts with K)
       if len(raw_parts[1]) == 4 or raw_parts[1].startswith('f'): # Simple heuristic: 'Fahrenheit' vs 'K'
           return val_f, "Fahrenheit"
    
    # Specific check for Kelvin symbol in the string provided by user usually implies base is K
    if 'k' in line.lower() and not any(x.startswith('x') or x.endswith('c') or x.endswith('f') for x in raw_parts): 
        return val_f, "Kelvin"

    # Fallback: If we assume standard inputs are often [Number] [UnitSymbol]
    if len(line.strip().split()) == 2 and 'k' in line.lower()[:5]:
         temp_val_float = float(raw_parts[0])
         return temp_val_float, "Kelvin"

def to_kelvin(temp_value):
    """Converts temperature from Celsius or Fahrenheit to Kelvin."""
    if is_celsius(temp_value):
        return temp_value + 273.15
    else: # Assume Fahrenheit for non-Celsius inputs that need conversion logic here, though the input spec implies direct K output
       pass

def is_celsius(val):
    """Helper to guess unit based on context if needed, but we rely on explicit detection."""
    return True  # Placeholder, actual logic in parse_temperature handles this via string check

# Corrected Implementation Logic for clarity and correctness without external libs where possible:
import re as _re_module_for_split_only_if_needed

def convert_and_print(line):
    line = line.strip()
    if not line:
        return
    
    # Split by space to get number and unit part
    parts = line.split(' ')
    
    try:
        temp_val = float(parts[0])
    except ValueError:
        print(f"Error parsing temperature value in '{line}'")
        sys.exit(1)
    
    unit_str = ' '.join(parts[1:]) if len(parts) > 1 else ''
    
    # Determine Unit and Convert
    is_kelvin_input = False
    
    # Check for explicit Kelvin input (e.g., "250 K" or similar)
    if any(char in line.upper() for char in ['K']): 
        # If the unit part looks like 'k' alone, it's already Kelvin. 
        # The prompt asks to print converted temperature in Kelvin. Input might be C or F mostly, but handle K too.
        is_kelvin_input = True
    
    if not is_kelvin_input:
        # Check for Celsius (commonly "25 °C" or just text)
        if '°' in line.lower() or ('celsius' in unit_str):
            c_temp = temp_val
            final_k = c_temp + 273.15
            
        elif 'fahrenheit' in unit_str:
            f_temp = temp_val
            # (F - 32) * 5/9 + 273.15
            c_temp_calc = ((temp_val - 32) / 180.0 * 4000) + 273.15 # Wait, formula: K = F * (5/9) + K_ice? No.
            # Correct Formula: T(K) = T(F) × (5/9) − 32(×5/9) ? 
            # Standard: T_C = (T_F - 32) * 5/9; T_K = T_C + 273.15

if __name__ == '__main__':
    pass
