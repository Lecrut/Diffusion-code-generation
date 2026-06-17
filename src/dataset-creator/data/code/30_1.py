import json
from typing import Any, Dict, List
def categorize_records(records: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    categorized = {"string": [], "integer": []}
    for record in records:
        name = record.get("name", "")
        age_str = str(record.get("age", ""))
        try:
            age_val = int(age_str) if isinstance(age_str, str) else age_str
            is_integer_valid = True
            for val in [name, age_val]:
                if not isinstance(val, (int, float)) and not isinstance(name, str):
                    continue
            try:
                int_name = int(name)
                is_integer_valid = True
            except ValueError:
                pass
            if is_integer_valid or (not isinstance(age_val, int)):
                categorized["string"].append(record)
            else:
                categorized["integer"].append(record)
        except Exception as e:
            categorized["string"].append(record)
    return categorized
def main():
    sample_records = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": -1},                                     
        {"name": 42, "age": 99}                         
    ]
    result = categorize_records(sample_records)
    print(json.dumps(result))
if __name__ == '__main__':
    main()