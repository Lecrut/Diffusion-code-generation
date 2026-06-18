import csv
import json
from io import StringIO
def generate_csv_data():
    return [
        {"id": 101, "name": "Alice", "score": 95},
        {"id": 102, "name": "Bob", "score": 87},
        {"id": 103, "name": "Charlie", "score": 92}
    ]
def transform_to_json(csv_data):
    return json.dumps(csv_data)
if __name__ == '__main__':
    raw_csv = generate_csv_data()
    output_json = transform_to_json(raw_csv)
    csv_output_writer = csv.DictWriter(StringIO(), fieldnames=raw_csv[0].keys())
    csv_output_writer.writeheader()
    for row in raw_csv:
        csv_output_writer.writerow(row)
    print("JSON Output:")
    print(output_json)
    json_string_io = StringIO(output_json)
    parsed_data = json.load(json_string_io)
    csv_file_content = "id,name,score\n" + "\n".join([f"{r['id']},{r['name']},{r['score']}" for r in raw_csv])
    print("CSV Output:")
    print(csv_file_content)