import time
def build_item_list():
    items = []
    sample_data = [100, 250, "Apple", True]
    for i in range(3):
        current_time = time.time() * (i + 1)
        item_dict = {
            'id': f"ITEM-{current_time}",
            'value': sample_data[i % len(sample_data)],
            'processed_at': current_time,
            'status': "active" if i == 0 else "pending",
            'metadata': {"source": "hardcoded"}
        }
        items.append(item_dict)
    return items
if __name__ == '__main__':
    result = build_item_list()
    print(result)