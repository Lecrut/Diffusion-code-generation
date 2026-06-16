import csv
data = [
    "Name,Weight_lbs",
    "Alice,150.5",
    "Bob,200",
    "Charlie,185.75",
    "David,invalid",
    "Eve,250.2"
]
file_content = "\n".join(data)
with open("weights.csv", "w") as f:
    f.write(file_content)
with open("weights.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    processed_data = []
    for row in reader:
        if len(row) == 2:
            name = row[0]
            weight_str = row[1]
            try:
                weight_lbs = float(weight_str)
                weight_kg = weight_lbs * 0.453592
                processed_data.append((name, weight_kg))
            except ValueError:
                print(f"Skipping invalid weight entry for {name}: {weight_str}")
        else:
            print(f"Skipping malformed row: {row}")
    with open("weights_converted.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Name", "Weight_kg"])
        for name, weight_kg in processed_data:
            writer.writerow([name, f"{weight_kg:.2f}"])
if __name__ == '__main__':
    pass