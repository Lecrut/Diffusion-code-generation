import csv
def read_and_update_csv(input_file: str) -> list[list[str]]:
    records = []
    with open(input_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and not all(cell.strip() == '' for cell in row):
                records.append([cell.strip() for cell in row])
    return records
def write_updated_csv(records: list[list[str]], output_file: str, update_index: int = None, new_value: str | None = None) -> bool:
    if not records or len(records[0]) == 0:
        print("No valid data to process.")
        return False
    temp_records = [row[:] for row in records]
    if update_index is not None and 0 <= update_index < len(temp_records):
        target_row = temp_records[update_index][:]
        if new_value:
            try:
                int(new_value)
                target_row[int(target_row.index('ID')) - 1] = str(int(new_value))
            except ValueError:
                pass
            for i, cell in enumerate(target_row):
                try:
                    float(cell)
                    target_row[i] = f"{float(cell)}" if not new_value else None
                except (ValueError, IndexError):
                    continue
        temp_records[update_index] = [str(x).strip() if x is not None else '' for x in target_row]
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(temp_records)
    return True
if __name__ == '__main__':
    sample_data = [
        ['ID', 'Name', 'Age'],
        ['101', 'Alice', '30'],
        ['102', 'Bob', '25'],
        ['103', 'Charlie', '35']
    ]
    with open('input.csv', 'w') as f:
        writer = csv.writer(f)
        for row in sample_data:
            writer.writerow(row)
    records = read_and_update_csv('input.csv')
    update_index = 1
    new_value = "32"
    if write_updated_csv(records, 'output.csv', update_index=update_index, new_value=new_value):
        print("CSV updated successfully.")