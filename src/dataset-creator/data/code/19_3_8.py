import csv
import json
from io import StringIO
def generate_csv_data():
    return [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 87},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
def transform_to_json(csv_data):
    return [json.dumps(row) for row in csv_data]
if __name__ == '__main__':
    raw_csv = generate_csv_data()
    output_buffer = StringIO()
    writer = csv.DictWriter(output_buffer, fieldnames=raw_csv[0].keys())
    writer.writeheader()
    writer.writerows(raw_csv)
    json_output = transform_to_json(raw_csv)
    print(json.dumps(json_output))