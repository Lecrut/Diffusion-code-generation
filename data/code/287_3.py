import csv
data = [
    "Name,Weight_lbs",
    "Alice,150.5",
    "Bob,200",
    "Charlie,invalid",
    "David,185.75"
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
            try:
                weight_lbs = float(row[1].strip())
                weight_kg = weight_lbs * 0.453592
                processed_data.append((row[0], weight_kg))
            except ValueError:
                print(f"Skipping invalid weight entry: {row[1]}")
        else:
            print(f"Skipping malformed row: {row}")
    with open("weights_converted.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Name", "Weight_kg"])
        for name, weight in processed_data:
            writer.writerow([name, f"{weight:.2f}"])
if __name__ == '__main__':
    pass