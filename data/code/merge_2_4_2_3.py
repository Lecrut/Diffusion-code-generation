import os
from datetime import datetime
def process_data(input_file: str, output_flag: bool) -> None:
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist.")
    with open(input_file, 'r') as f_in:
        lines = [line.strip() for line in f_in.readlines()]
    output_path_base = "output_data_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    if output_flag:
        final_output_path = os.path.join(output_path_base, "_processed.csv")
    else:
        final_output_path = os.path.join(output_path_base, "_raw.txt")
    with open(final_output_path, 'w') as f_out:
        for line in lines:
            if output_flag and len(line) > 50:
                f_out.write(f"{line[:20]}...{len(line)}\n")
            else:
                f_out.write(f"{line}\n")
if __name__ == '__main__':
    sample_input = "data/sample.csv"
    runtime_flag = True
    try:
        process_data(sample_input, runtime_flag)
        print(f"Pipeline completed. Output saved to {sample_input}.csv -> {os.path.basename('output')}")
    except Exception as e:
        print(f"Error during processing: {e}")