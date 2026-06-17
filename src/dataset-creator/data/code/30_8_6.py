import json
def process_data():
    records = [
        {"id": 101, "value": 50, "metadata": {"category": "electronics", "source": "a"}},
        {"id": 102, "value": 30, "metadata": {"category": "clothing", "source": "b"}},
        {"id": 103, "value": 50, "metadata": {"category": "electronics", "source": "c"}},
        {"id": 104, "value": 20, "metadata": {"category": "clothing", "source": "d"}}
    ]
    categories = {}
    for item in records:
        cat = item["metadata"]["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
    return list(categories.values())
if __name__ == '__main__':
    result_groups, sorted_records = process_data()