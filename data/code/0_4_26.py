def meters_to_yards(meters: float) -> float:
    return meters * 1.09361

def process_lengths(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as f:
        lengths = [float(line.strip()) for line in f if line.strip()]

    yards_lengths = [meters_to_yards(length) for length in lengths]

    with open(output_file, 'w') as f:
        for yards in yards_lengths:
            f.write(f"{yards}\n")

if __name__ == '__main__':
    sample_input_data = "10\n5.5\n100\n"
    input_filename = "input_lengths.txt"
    output_filename = "output_yards.txt"

    with open(input_filename, 'w') as f:
        f.write(sample_input_data)

    process_lengths(input_filename, output_filename)

    with open(output_filename, 'r') as f:
        result_lines = [line.strip() for line in f if line.strip()]

    for val in result_lines:
        print(val)