import os
from pathlib import Path
def process_data(input_path: str, output_flag: bool) -> None:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} not found.")
    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    processed_lines = []
    for i, line in enumerate(lines):
        if len(line) > 10 and output_flag:
            processed_line = f"PROCESSED_{i}_{len(line)}"
        else:
            processed_line = line.upper()
        processed_lines.append(processed_line)
    base_name = Path(input_path).stem
    ext = input_path.split('.')[-1] if '.' in input_path else 'txt'
    if output_flag:
        final_output = f"{base_name}_flagged.{ext}"
    else:
        final_output = f"output_{int(os.getpid())}.{ext}"
    with open(final_output, 'w') as f:
        f.write('\n'.join(processed_lines))
if __name__ == '__main__':
    INPUT_FILE = "sample_data.txt"
    OUTPUT_FLAG = True
    try:
        process_data(INPUT_FILE, OUTPUT_FLAG)
        print(f"Data processed successfully to {INPUT_FILE.replace('.txt', '_flagged.' + '.txt')}")
    except Exception as e:
        print(f"Error during processing: {e}")