import json
import csv
def count_items(data_source):
    if isinstance(data_source, str) and data_source.endswith('.json'):
        try:
            with open(data_source, 'r') as f:
                content = json.load(f)
                return len(content.get('items', []))
        except (json.JSONDecodeError, FileNotFoundError):
            return 0
    elif isinstance(data_source, str) and data_source.endswith('.csv'):
        try:
            with open(data_source, 'r') as f:
                reader = csv.DictReader(f)
                items_count = sum(1 for _ in reader if _.get('item_id'))
                return items_count
        except (FileNotFoundError):
            return 0
    else:
        try:
            with open(data_source, 'r') as f:
                content = json.load(f)
                return len(content.get('items', []))
        except Exception:
            return 0
if __name__ == '__main__':
    sample_json_str = '{"items": [{"id": "1"}, {"id": "2"}]}'
    sample_csv_str = "item_id,description\n1,item one\n2,item two"
    json_data = {'items': [{'id': 'a'}, {'id': 'b'}]}
    csv_data = [
        ['item_id', 'name'],
        ['x', 'first'],
        ['y', 'second']
    ]
    print(f"JSON Count: {count_items(json_data)}")
    print(f"CSV Count (parsed list): {sum(1 for row in csv_data if len(row) > 0 and row[0] != '')}")