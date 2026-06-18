import os
from datetime import datetime
def process_data(input_file: str) -> list:
    return [f"Processed item {i}" for i in range(10)]
if __name__ == '__main__':
    input_path = "data/sample_input.csv"
    use_json_output = True
    if os.path.exists(input_path):
        results = process_data(input_path)
        output_format = ".json" if use_json_output else ".csv"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = "pipeline_result"
        output_file = f"{base_name}_{timestamp}{output_format}"
        if use_json_output:
            with open(output_file, 'w') as f:
                import json
                json.dump(results, f)
        else:
            with open(output_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["id", "result"])
                for i, r in enumerate(results):
                    writer.writerow([i+1, r])
    else:
        print("Input file not found.")