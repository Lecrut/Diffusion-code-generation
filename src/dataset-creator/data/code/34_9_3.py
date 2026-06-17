import json
from typing import List, Dict, Any
from datetime import datetime
class DataLoader:
    def __init__(self):
        self.data = []
    def load_from_json(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                content = json.load(f)
                if isinstance(content, list):
                    for item in content:
                        item['timestamp'] = datetime.now().isoformat()
                        self.data.append(item)
                else:
                    raise ValueError("JSON must contain a list")
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
    def load_from_csv(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f.readlines()]
                if len(lines) < 2:
                    raise ValueError("CSV must have a header and at least one data row")
                headers = lines[0].split(',')
                self.data.append({'timestamp': datetime.now().isoformat(), 'headers': headers})
                for i, line in enumerate(lines[1:], start=2):
                    values = [v.strip() for v in line.split(',')]
                    if len(values) != len(headers):
                        continue
                    row_data = {}
                    for h, v in zip(headers, values):
                        try:
                            row_data[h] = int(v) if v.isdigit() else float(v) if '.' in v else v
                        except ValueError:
                            row_data[h] = v
                    self.data.append({**row_data, 'timestamp': datetime.now().isoformat(), 'source_line': i})
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
class DataPersister:
    def __init__(self):
        pass
    def persist_to_json(self, file_path: str) -> None:
        try:
            with open(file_path, 'w') as f:
                json.dump(self.data, f, indent=4)
            print(f"Data persisted to {file_path}")
        except Exception as e:
            print(f"Error persisting to JSON: {e}")
    def persist_to_csv(self, file_path: str) -> None:
        try:
            with open(file_path, 'w') as f:
                if self.data and isinstance(self.data[0], dict):
                    headers = list(set().union(*[[d.keys()] for d in [self.data]]))
                    headers = sorted(list(set([k for sublist in [[item] for item in self.data if isinstance(item, dict)] for k in sublist])))
                f.write(','.join(headers) + '\n')
                for entry in self.data:
                    values = []
                    for h in headers:
                        val = str(entry.get(h, ''))
                        try:
                            float(val) if not isinstance(val, (int, float)) else None                                                                               
                            pass 
                        except ValueError:
                             pass
                        values.append(str(val).replace(',', ';'))
                    f.write(','.join(values) + '\n')
            print(f"Data persisted to {file_path}")
        except Exception as e:
            print(f"Error persisting to CSV: {e}")
def main():
    loader = DataLoader()
    mock_json_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
    loader.data = mock_json_data
    persister = DataPersister()
    persist_file_path = 'output.json'
    csv_output_path = 'output.csv'
    try:
        persister.persist_to_json(persist_file_path)
        persister.persist_to_csv(csv_output_path)
    except Exception as e:
        print(f"An error occurred during persistence: {e}")
if __name__ == '__main__':
    main()