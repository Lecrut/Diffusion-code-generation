import math

def read_lengths_from_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    lengths = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            value = float(stripped)
            lengths.append(value)
    return lengths

def meters_to_yards(meters):
    return meters * 1.09361

def convert_lengths(meters_list):
    yards_list = []
    for meters in meters_list:
        yards = meters_to_yards(meters)
        yards_list.append(yards)
    return yards_list

if __name__ == '__main__':
    sample_data = [1.0, 5.0, 100.0]
    temp_filepath = '/tmp/lengths_input.txt'
    with open(temp_filepath, 'w') as temp_file:
        for length in sample_data:
            temp_file.write(f'{length}\n')
    
    input_lengths = read_lengths_from_file(temp_filepath)
    output_lengths = convert_lengths(input_lengths)
    
    for i in range(len(input_lengths)):
        print(f'{input_lengths[i]} meters is {output_lengths[i]} yards')