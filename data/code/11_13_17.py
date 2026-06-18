import sys

def validate_positive_number(value):
    """Check if a string represents a positive number."""
    try:
        num = float(value)
        return num > 0, num
    except ValueError:
        return False, None

def calculate_ratio(length_a, length_b):
    """Calculate the ratio of two lengths and return it as (numerator/denominator)."""
    if length_b == 0:
        raise ValueError("Denominator cannot be zero.")
    
    numerator = length_a / length_b
    denominator = 1
    
    # Simplify fraction by finding GCD
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(int(numerator), int(denominator)) if numerator == int(numerator) else None
    if common_divisor is not None and denominator != 0:
        simplified_numerator = int(numerator / common_divisor)
        simplified_denominator = int(1 / common_divisor)
        
        # Check for integer result
        remainder = (int(numerator * 100) % 100) // 10 if float(int(numerator)) != numerator else 0
        
    return f"{numerator:.2f}"

def format_output(label, num_str):
    """Format the output string clearly."""
    print(f"Ratio of {label}:")
    parts = [str(num_str)]
    
    # Check if it's a whole number or has decimals to decide formatting
    try:
        val = float(num_str)
        is_whole = abs(val - round(val)) < 1e-9
        
        if not is_whole and num_str.count('.') == 0:
            parts.append(" (whole)")
            
    except ValueError:
        pass
    
    print(f"  Result: {' / '.join(parts)}")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    length_a_str = "12.0"
    length_b_str = "4.0"

    try:
        val_a, num_a = validate_positive_number(length_a_str)
        if not val_a:
            raise ValueError("Input must be a positive number.")
            
        val_b, num_b = validate_positive_number(length_b_str)
        if not val_b:
            raise ValueError("Input must be a positive number.")

        ratio_result = f"{num_a / num_b:.2f}"
        
    except Exception as e:
        print(f"Error processing inputs: {e}", file=sys.stderr)
        sys.exit(1)

    format_output("Length A", ratio_result)