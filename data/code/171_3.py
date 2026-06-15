import csv
data = [
    ["id", "name", "price"],
    ["1", "Laptop", "1200.50"],
    ["2", "Mouse", "25.99"],
    ["3", "Keyboard", "75.00"],
    ["4", "Monitor", "300.75"]
]
store = []
header = []
data_rows = []
if data:
    header = data[0]
    data_rows = data[1:]
for row in data_rows:
    if len(row) == len(header):
        record = {}
        is_valid = True
        for i, field in enumerate(header):
            record[field] = row[i].strip() if row[i] else None
            if record[field] is None:
                is_valid = False
                break
        if is_valid:
            store.append(record)
if __name__ == '__main__':
    print(store)