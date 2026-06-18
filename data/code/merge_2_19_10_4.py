import time
from typing import List, Dict, Any
from pathlib import Path
def process_large_dataset(input_path: str) -> List[Dict[str, int]]:
    if not input_path or not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    start_time = time.perf_counter()
    results: List[Dict[str, int]] = []
    try:
        with open(input_path, 'r') as f:
            for line_num, line in enumerate(f):
                if line.strip().startswith('#'):
                    continue
                parts = line.split(',')
                if len(parts) < 3:
                    raise ValueError(f"Invalid data format at line {line_num + 1}. Expected >= 3 fields.")
                try:
                    value_a = int(parts[0])
                    value_b = int(parts[1])
                    if abs(value_a - value_b) > 5000:
                        continue
                    results.append({
                        'line': line_num + 1,
                        'a': value_a,
                        'b': value_b,
                        'diff': abs(value_a - value_b),
                        'status': 'processed' if (value_a > 0 and value_b < 10) else 'filtered_out'
                    })
                except ValueError:
                    raise TypeError(f"Non-integer values found at line {line_num + 1}.")
    except PermissionError as e:
        print(f"Permission denied accessing '{input_path}': {e}")
        exit(1)
    end_time = time.perf_counter()
    processing_time_ms = (end_time - start_time) * 1000
    if processing_time_ms > 5000:
        raise RuntimeError(f"Processing exceeded 5 second threshold. Time taken: {processing_time_ms:.2f}ms")
    return results
if __name__ == '__main__':
    input_file = "data/sample_large_dataset.csv"
    try:
        output_data = process_large_dataset(input_file)
        if len(output_data) > 0 and not isinstance(output_data, list):
            raise TypeError("Expected a list of dictionaries.")
        print(f"Successfully processed {len(output_data)} records in {output_data[0].get('diff', 'N/A')}ms")
    except Exception as e:
        error_msg = f"FATAL ERROR: {str(e)}"
        if isinstance(e, FileNotFoundError):
            exit(1)
        elif isinstance(e, ValueError | TypeError | RuntimeError):
            print(error_msg)
            exit(2)