import csv
from pathlib import Path
def load_dataset(file_path: str) -> list[dict]:
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Dataset file '{file_path}' not found.")
    records = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_row = {key.strip(): value.strip() if isinstance(value, str) else value 
                          for key, value in row.items()}
            records.append(cleaned_row)
    return records
def check_name_existence(name_to_find: str, dataset_records: list[dict]) -> bool:
    if not isinstance(dataset_records, list):
        raise TypeError("Dataset must be a list of dictionaries.")
    target_lower = name_to_find.lower().strip()
    for record in dataset_records:
        for field_name, value in record.items():
            if isinstance(value, str):
                if value.lower().strip() == target_lower or target_lower in value.lower():
                    return True
    return False
def main():
    dataset_file = "sample_data.csv"
    search_name = "Alice"
    try:
        records = load_dataset(dataset_file)
        if not check_name_existence(search_name, records):
            print(f"Name '{search_name}' was NOT found in the dataset.")
        else:
            print(f"Name '{search_name}' WAS found in the dataset.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {str(e)}")
if __name__ == '__main__':
    main()