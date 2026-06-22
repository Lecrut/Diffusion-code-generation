import csv

def scale_volumes(input_file, output_file, scale_factor):
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if len(row) == 2:
                item_name, volume = row
                scaled_volume = float(volume) * scale_factor
                writer.writerow([item_name, scaled_volume])

if __name__ == '__main__':
    input_data = """item1,10.5
item2,20.3
item3,30.7"""
    
    with open('input.csv', 'w') as f:
        f.write(input_data)
    
    scale_factor = 1.5
    output_file = 'output.csv'
    
    scale_volumes('input.csv', output_file, scale_factor)
    
    with open(output_file, 'r') as f:
        print(f.read())