def convert_meters_to_yards(meters_list):
    meters_to_yards_factor = 1.09361
    return [m * meters_to_yards_factor for m in meters_list]

def read_lengths_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lengths = []
    for line in lines:
        line = line.strip()
        if line:
            lengths.append(float(line))
    return lengths

def process_lengths(input_filename, output_values):
    meters = read_lengths_from_file(input_filename)
    yards = convert_meters_to_yards(meters)
    for m, y in zip(meters, yards):
        output_values.append((m, y))

if __name__ == '__main__':
    sample_data = [100, 50, 0.5, 1.8288]
    
    import tempfile
    import os
    
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
    for length in sample_data:
        temp_file.write(f"{length}\n")
    temp_file.close()
    
    result_list = []
    process_lengths(temp_file.name, result_list)
    
    for m, y in result_list:
        print(y)
    
    os.unlink(temp_file.name)