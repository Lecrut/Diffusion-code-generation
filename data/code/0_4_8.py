def convert_meters_to_yards(meters_list):
    result = []
    for meters in meters_list:
        yards = meters * 1.09361
        result.append(yards)
    return result

def process_lengths(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        lines = f.readlines()
    meters_list = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            meters_list.append(float(stripped))
    yards_list = convert_meters_to_yards(meters_list)
    with open(output_file_path, 'w') as f:
        for yards in yards_list:
            f.write(f"{yards}\n")
    return yards_list

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 10.0]
    yards_values = convert_meters_to_yards(sample_lengths)
    for val in yards_values:
        print(val)