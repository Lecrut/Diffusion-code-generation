import json
from typing import List, Dict, Any
import sqlite3
import os
class DataLoader:
    def __init__(self):
        self.storage_backends = {}
    def load_from_json(self, file_path: str) -> List[Dict[str, Any]]:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return [item for item in data if isinstance(item, dict)]
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            raise
    def load_from_csv(self, file_path: str) -> List[Dict[str, Any]]:
        try:
            import csv
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            raise
    def persist_to_sqlite(self, data_list: List[Dict[str, Any]], db_file: str):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, value REAL)")
        except Exception as e:
            print(f"Database creation error: {e}")
        insert_query = "INSERT INTO entries (name, value) VALUES (?, ?)"
        for item in data_list:
            if 'name' in item and 'value' in item:
                try:
                    cursor.execute(insert_query, (item['name'], float(item.get('value', 0))))
                except ValueError as ve:
                    print(f"Invalid value format for {item}: {ve}")
        conn.commit()
        conn.close()
def main():
    json_data = [
        {"name": "Alice", "value": 10.5},
        {"name": "Bob", "value": 20.3}
    ]
    csv_data = [
        ["Charlie", 30.7],
        ["David", 40.1]
    ]
    loader = DataLoader()
    db_file = "sample_database.db"
    try:
        loader.persist_to_sqlite(json_data, db_file)
        print(f"Successfully persisted {len(json_data)} records from simulated JSON source.")
        csv_dict_list = [dict(row) for row in csv_data]
        loader.persist_to_sqlite(csv_dict_list, db_file)
        print("Successfully persisted records from simulated CSV source.")
    except Exception as e:
        print(f"An error occurred during persistence: {e}")
if __name__ == '__main__':
    main()