import csv
def convert_to_kg(file_path, output_path):
    weights_in_kg = []
    with open(file_path, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader, None)
        if header is None:
            return
        for row in reader:
            try:
                weight_value = float(row[0].strip())
                unit = row[1].strip().lower()
                if unit in ['kg', 'kilogram', 'kgr']:
                    weights_in_kg.append(weight_value)
                elif unit in ['lb', 'lbs', 'pound']:
                    weight_in_kg = weight_value * 0.453592
                    weights_in_kg.append(weight_in_kg)
                else:
                    print(f"Skipping row due to unknown unit: {row}")
            except ValueError:
                print(f"Skipping row due to invalid weight format: {row}")
            except IndexError:
                print(f"Skipping row due to insufficient columns: {row}")
    with open(output_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        header = header
        writer.writerow(header)
        for weight in weights_in_kg:
            writer.writerow([weight])
if __name__ == '__main__':
    sample_input_file = 'weights_input.csv'
    sample_output_file = 'weights_output_kg.csv'
    with open(sample_input_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Weight'])
        writer.writerow(['10.5', 'kg'])
        writer.writerow(['150', 'lbs'])
        writer.writerow(['2.1', 'kilogram'])
        writer.writerow(['invalid', 'kg'])
        writer.writerow(['300', 'grams'])
    convert_to_kg(sample_input_file, sample_output_file)