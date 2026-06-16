import csv
def load_definitions(file_path: str) -> dict[str, list[str]]:
    definitions = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if not row or len(row) < 2:
                continue
            word = row[0].strip()
            def_list = [item.strip() for item in row[1:] if item.strip()]
            definitions[word] = def_list
    return definitions
if __name__ == '__main__':
    data_file = 'sample_data.csv'
    dictionary = load_definitions(data_file)