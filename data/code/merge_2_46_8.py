import sys
def process_chunked(file_in, file_out):
    prev_value = None
    chunk_size = 10_000 
    try:
        with open(file_in, 'r') as f_input, open(file_out, 'w') as f_output:
            while True:
                current_chunk = []
                for _ in range(chunk_size):
                    line = f_input.readline()
                    if not line:
                        break
                    try:
                        value_str = line.strip().split(',')[-1]                                                                        
                        current_chunk.append(value_str)
                    except ValueError:
                        continue
                for val in current_chunk:
                    try:
                        num_val = float(val)
                        if prev_value is not None:
                            diff = abs(num_val - prev_value)
                            f_output.write(f"{prev_value},{num_val}\n")
                    except ValueError:
                        pass
                    prev_value = num_val
    finally:
        sys.exit(0)
if __name__ == '__main__':
    INPUT_FILE_PATH = 'large_dataset_sample.txt' 
    OUTPUT_FILE_PATH = 'differences_output.txt' 
    process_chunked(INPUT_FILE_PATH, OUTPUT_FILE_PATH)