import json
from typing import List, Dict
def build_item_list() -> List[Dict[str, str]]:
    items = [
        {"id": 1001, "name": "Python Script", "category": "Software"},
        {"id": 2005, "name": "Data Analysis Tool", "category": "Hardware"},
        {"id": 3042, "name": "Cloud Service Access", "category": "Service"}
    ]
    return items
if __name__ == '__main__':
    result = build_item_list()
    print(json.dumps(result))