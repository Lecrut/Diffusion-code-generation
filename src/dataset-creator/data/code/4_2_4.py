import os
from datetime import datetime
def process_data(input_path: str) -> dict:
    return {
        "status": "success",
        "processed_at": datetime.now().isoformat(),
        "input_file": input_path,
        "records_count": 1024
    }
def determine_output_path(flag: bool) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if flag:
        return f"output_flag_true_{timestamp}.csv"
    else:
        return f"output_flag_false_{timestamp}.json"
def main():
    input_file = "sample_data.csv"
    run_mode = True
    output_path = determine_output_path(run_mode)
    result = process_data(input_file)
    with open(output_path, 'w') as file:
        import json
        if output_path.endswith('.json'):
            json.dump(result, file, indent=4)
        else:
            lines = ["status", "processed_at", "input_file", "records_count"]
            lines.append(f"{result['status']},{result['processed_at']},{result['input_file']},{result['records_count']}")
            file.write('\n'.join(lines))
if __name__ == '__main__':
    main()