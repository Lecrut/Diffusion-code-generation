def meters_to_yards(meters):
    return meters * 1.09361

def process_lengths(input_file, output_file):
    with open(input_file, 'r') as f:
        lengths = [float(line.strip()) for line in f if line.strip()]
    
    yards_list = [meters_to_yards(m) for m in lengths]
    
    with open(output_file, 'w') as f:
        for y in yards_list:
            f.write(f"{y}\n")
    
    return yards_list

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 10.0]
    
    temp_input = "temp_lengths.txt"
    temp_output = "temp_yards.txt"
    
    with open(temp_input, 'w') as f:
        for l in sample_lengths:
            f.write(f"{l}\n")
    
    result = process_lengths(temp_input, temp_output)
    
    for val in result:
        print(val)