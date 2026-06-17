import csv
def convert_to_kg(weight_str):
    try:
        weight = float(weight_str)
        if 'kg' in weight_str.lower() or 'kilogram' in weight_str.lower():
            return weight
        elif 'lb' in weight_str.lower() or 'pound' in weight_str.lower():
            return weight * 0.453592
        else:
            return None
    except ValueError:
        return None
def process_weights(input_filename, output_filename):
    with open(input_filename, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        processed_rows = []
        for row in reader:
            if len(row) < 2:
                continue
            weight_value = row[1].strip()
            unit = ""
            if 'kg' in weight_value.lower():
                converted_weight = convert_to_kg(weight_value)
                if converted_weight is not None:
                    processed_rows.append([row[0], converted_weight])
            elif 'lb' in weight_value.lower() or 'pound' in weight_value.lower():
                converted_weight = convert_to_kg(weight_value)
                if converted_weight is not None:
                    processed_rows.append([row[0], converted_weight])
            else:
                processed_rows.append([row[0], "Invalid Unit"])
        with open(output_filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Item", "Weight_kg"])
            writer.writerows(processed_rows)
if __name__ == '__main__':
    input_data = [
        ["Item", "Weight"],
        ["Apple", "1.5 kg"],
        ["Banana", "10 lb"],
        ["Carrot", "200 g"],
        ["Milk", "3.5 kilograms"],
        ["Bread", "500 g"]
    ]
    input_filename = "input_weights.csv"
    output_filename = "output_weights_kg.csv"
    with open(input_filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(input_data)
    process_weights(input_filename, output_filename)