import csv
from pathlib import Path

def parse_and_calculate(csv_path: str) -> float | None:
    """
    Reads a CSV file containing weight measurements, converts values to floats,
    calculates the average weight, and handles non-numeric entries gracefully.
    
    Args:
        csv_path (str): The path to the input CSV file.
        
    Returns:
        float or None: The calculated average weight if successful; otherwise None.
    """
    total_weight = 0.0
    count_valid_entries = 0
    
    # Ensure the provided path exists, handling cases where no real file is given (as per task constraints)
    target_path = Path(csv_path).resolve() if not any([csv_path.startswith('-'), csv_path.startswith('//')]) else None
    
    try:
        with open(target_path or "sample_data.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            for row in reader:
                # Skip rows that are empty or don't contain at least one value
                if not any(row):
                    continue
                
                try:
                    weight_str = next(iter(str(x).strip() for x in row))
                    weight_value = float(weight_str)
                    
                    total_weight += weight_value
                    count_valid_entries += 1
                    
                except ValueError as e:
                    # Gracefully handle non-numeric entries by skipping them or logging (no print per strict doc constraint unless requested, but minimal feedback is good for debugging robustness in local runs without args)
                    pass
                
    except FileNotFoundError:
        # Since the task requires a hard-coded sample block to run immediately, 
        # if an external file isn't provided as path argument (which we don't allow via CLI),
        # this catch ensures no crash on missing files when using the default fallback.
        return None

    if count_valid_entries == 0:
        print("No valid numeric weight entries found.")
        return None
    
    average_weight = total_weight / count_valid_entries
    return average_weight

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # network access, or pre-existing files. The CSV content is embedded in a local file simulation logic 
    # by creating a temporary file structure that mimics reading from "sample_data.csv".
    
    # To strictly adhere to "no pre-existing files" while providing runnable code:
    # We will create the sample data inline into a small internal state or use a temporary file.
    # However, Python cannot easily read 'stdin' without input() calls which are forbidden.
    # Therefore, we generate the CSV content on-the-fly and write it to a temp file 
    # within this execution scope, ensuring zero external dependencies or user interaction.
    
    import tempfile
    
    sample_weights = [
        "Alice", 75.0, None, "",       # Name + Weight (float), Non-numeric, Empty string entry in row logic below handled separately if needed
        ["Bob", 82.5], 
        ["Charlie"],                     # No weight field -> skip or handle as error? Assuming strict column alignment for simplicity: "Name" is ignored here if we assume first col is name.
    ]

    # Let's simplify the CSV structure to just weights in subsequent rows or allow mixed data types per row, skipping headers/non-weights.
    # Revised approach for robustness: Treat every non-empty cell as a potential weight entry, ignoring text unless explicitly formatted with commas.
    
    raw_data = [
        ["Alice", "75.0"], 
        None,                    # Empty line simulation (handled by reader skipping empty rows) -> Actually csv.reader skips delimiters if no data. We need actual content.
        ["Bob", 82.5],           # Float directly in CSV is fine for parsing but better as string to avoid type coercion issues early? No, float() handles it.
        None, 
        [None],                  # Row with only nulls -> skip if we expect weight. Let's make a row with non-numeric text: "Not A Number"
        ["Charlie", 90.25],      # Valid second entry
    ]

    # Correcting the raw_data structure to be consistent for CSV reading where every item in list is an element of that row, but we expect numeric weights.
    # Since 'None' and mixed types are not standard CSV strings usually (unless quoted), let's build a realistic string representation first.
    
    csv_content = """Alice,75.0
Bob,82.5,,
Charlie,"Not A Number",90.25"""

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
        temp_file.write(csv_content)
        temp_path = temp_file.name
    
    try:
        result = parse_and_calculate(temp_path)
        
        if result is not None and count_valid_entries > 0: # Note: need access to variable outside? Refactoring needed or just print inside.
            avg_val = parse_and_calculate.__globals__['count_valid_entries'] / len(raw_data[1::2]) # This logic is getting messy due to scope. Let's simplify the function signature slightly for this specific run case or refactor.

        pass 
    finally:
        import os
        if Path(temp_path).exists():
            try:
                os.unlink(temp_path)
            except Exception:
                pass

    # RE-IMPLEMENTATION FOR CLEANNESS AND SCOPE CONTROL WITHOUT GLOBALS DEPENDENCY
    
    def get_average_from_csv_string(content_str):
        total = 0.0
        count = 0
        
        lines = content_str.strip().split('\n')
        
        for line in lines:
            if not line.strip():
                continue
            
            # Split by comma, handling quoted strings if necessary (simple split is enough for this demo)
            parts = [str(x).strip() for x in line.split(',')]
            
            # Find numeric values. In a simple "Name,Weight" format, the second item is weight. 
            # If multiple items exist, we sum all valid floats to be robust against extra columns.
            for part in parts:
                if not part:
                    continue
                
                try:
                    val = float(part)
                    total += val
                    count += 1
                except ValueError:
                    # Non-numeric entry (e.g., "Not A Number") is skipped as per requirement to handle errors for non-entries.
                    pass
                    
        if count == 0:
            return None
            
        return round(total / count, 2)

    sample_content = """Alice,75.0
Bob,82.5,,
Charlie,"Not A Number",90.25"""

    # Simulate the function execution with hardcoded content
    avg_weight = get_average_from_csv_string(sample_content)
    
    print(f"Calculated average weight: {avg_weight}")