import sys

def parse_temperature_line(line: str) -> float | None:
    """Parses a line to extract temperature value and unit, returning Kelvin."""
    try:
        parts = line.strip().split()
        if len(parts) < 2 or not any(p.upper().startswith(('C', 'F')) for p in parts):
            return None

        value_str = ''
        unit_char = ''
        
        # Find the numeric part and the unit character
        try:
            idx_num = -1
            idx_unit = -1
            
            i = 0
            while i < len(parts) and not (parts[i].lstrip('-').isdigit() or parts[i][0] in '+-.'):
                # Skip non-numeric leading text if any, though format is usually "25 C"
                pass
                
            for j, part in enumerate(parts):
                try:
                    float(part)
                    idx_num = j
                except ValueError:
                    continue
            
            unit_char = parts[idx_num + 1].upper()[:3] if idx_num < len(parts) - 1 else ''

        except Exception:
            return None
        
        # Extract value from the numeric part string
        val_str_parts = []
        for p in parts:
            try:
                float(p.replace(',', '.'))
                val_str_parts.append(float(p.replace(',', '.')))
            except ValueError:
                continue
                
        if not val_str_parts or len(val_str_parts) != 1:
            return None
            
        temp_val = val_str_parts[0]

    except Exception:
        return None
    
    # Determine conversion logic based on unit found in parts (case insensitive check again for safety)
    has_celsius = any(p.upper() == 'C' or p.lower().startswith('c') and len(p) > 1 for p in parts if not p.replace('.', '').replace(',', '').isdigit())
    
    # Re-evaluate based on strict parsing of "Value Unit" format where unit is the last token starting with C/F
    temp_val = None
    value_found_idx = -1

if __name__ == '__main__':
    pass
