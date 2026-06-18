import sys

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    lines = [
        "0 C",
        "180 F"
    ]
    
    for line in lines:
        parts = line.strip().split()
        temp_str = parts[0]
        
        try:
            if len(parts) >= 2 and 'C' in parts[-1]:
                temperature = float(temp_str.replace(' ', '')) + 273.15
                print(f"{temperature} K")
            elif len(parts) == 2 and 'F' in parts[1]:
                # Handle cases like "0 F" or ensure unit is last part
                if parts[-1].endswith('F'):
                    temperature = (float(temp_str.replace(' ', '')) - 32) * 5 / 9 + 273.15
                    print(f"{temperature} K")
            else:
                # Fallback for simple "0 C" format where unit might be separate or combined if needed, 
                # but based on strict parsing of input like "0 C":
                if parts[-1] == 'C':
                    temperature = float(parts[0]) + 273.15
                    print(f"{temperature} K")
        except ValueError:
            continue