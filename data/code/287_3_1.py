import csv
data = [
    "Name,Weight_lbs",
    "Alice,150.5",
    "Bob,200",
    "Charlie,invalid",
    "David,185.75"
]
with open("weights.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
input_filename = "weights.csv"
output_filename = "weights_kg.csv"
with open(input_filename, mode='r', newline='') as infile, \
     open(output_filename, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        if len(row) == 2:
            try:
                weight_lbs = float(row[1].strip())
                weight_kg = weight_lbs * 0.453592
                writer.writerow([row[0], f"{weight_kg:.2f}"])
            except ValueError:
                writer.writerow([row[0], "Invalid Data"])
        else:
            writer.writerow(row)
if __name__ == '__main__':
    pass