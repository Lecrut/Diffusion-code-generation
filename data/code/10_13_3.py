import sys

def parse_temperature(value_str: str) -> float | None:
    """Convert a string to a temperature value, returning None on failure."""
    try:
        return float(value_str.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    temp_a = 25.0
    temp_b = -10.5
    
    if parse_temperature(str(temp_a)) is not None and parse_temperature(str(temp_b)) is not None:
        t1, t2 = float(temp_a), float(temp_b)
        
        status = "A > B" if t1 > t2 else ("B > A" if t2 > t1 else "Equal")
        diff_str = f"{t1 - t2:+.1f}"
        
        print(f"T_A: {temp_a}, T_B: {temp_b} | Comparison: [{status}] (Diff: {diff_str})")