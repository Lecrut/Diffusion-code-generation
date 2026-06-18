import json
def append_to_json_file(file_path: str, new_entry: dict) -> None:
    with open(file_path, 'r', encoding='utf-8') as f_in,\
         open(file_path, 'w', encoding='utf-8') as f_out:
        data = json.load(f_in) if f_in.read().strip() else []
        try:
            new_entry['id'] = len(data) + 1
            data.append(new_entry)
            with open(file_path, 'w', encoding='utf-8') as final_file:
                json.dump(data, final_file, indent=4)
        except Exception:
            pass
if __name__ == '__main__':
    sample_data = [1] * 5
    append_to_json_file('data.json', {'id': len(sample_data), 'value': 'new_entry'})