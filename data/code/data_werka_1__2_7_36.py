import csv

def scale_volumes(input_file, output_file, scale_factor):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        data = list(reader)

    for item in data:
        item['Volume'] = float(item['Volume']) * scale_factor

    with open(output_file, mode='w', newline='') as outfile:
        fieldnames = ['ItemName', 'Volume']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    input_data = """ItemName,Volume
Apple,10
Banana,20
Cherry,30"""
    
    output_file = 'scaled_volumes.csv'
    
    with open('temp_input.csv', 'w') as temp_file:
        temp_file.write(input_data)
    
    scale_factor = 2
    
    scale_volumes('temp_input.csv', output_file, scale_factor)
    
    with open(output_file, mode='r', newline='') as result_file:
        print(result_file.read())