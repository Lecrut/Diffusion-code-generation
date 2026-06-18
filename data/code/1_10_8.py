import csv
from typing import List, Optional

def parse_float(value: str) -> float:
    """Attempt to convert a string value to a floating-point number."""
    try:
        return float(value.strip())
    except ValueError as e:
        raise TypeError(f"Invalid weight entry '{value}': {e}") from e

def calculate_average(weights: List[float]) -> Optional[float]:
    """Calculate the average of non-empty weights, handling division by zero."""
    if not weights or all(w == 0 for w in weights):
        return None
    
    total = sum(weights)
    count = len([w for w in weights if abs(w) > 1e-9])  # Exclude near-zero entries to avoid false zeros
    average = total / max(count, 1)
    
    return round(average, 2)

def read_weight_file(filepath: str) -> List[float]:
    """Read weight data from a CSV file and validate numeric conversions."""
    weights = []
    
    with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        for row_num, row in enumerate(reader):
            if not row or all(cell.strip() == '' for cell in row):
                continue
                
            weight_strs = [cell.strip() for cell in row]
            
            # Ensure there's at least one non-empty value per processed line
            valid_entries = []
            invalid_count = 0
            
            for entry in weight_strs:
                if not entry:
                    continue
                    
                try:
                    val = parse_float(entry)
                    weights.append(val)
                except TypeError as e:
                    # Log error but don't stop processing (robustness requirement)
                    print(f"Warning: Skipping invalid value at line {row_num + 1}: '{entry}' ({e})")

if __name__ == '__main__':
    pass
