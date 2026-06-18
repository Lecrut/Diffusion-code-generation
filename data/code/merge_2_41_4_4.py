from typing import List, Dict
def count_storage_items(containers: List[Dict[str, int]]) -> int:
    return sum(container.get("item_count", 0) for container in containers)
if __name__ == '__main__':
    sample_containers = [
        {"container_id": "A1", "item_count": 5},
        {"container_id": "B2", "item_count": 3},
        {"container_id": "C3", "item_count": 0}
    ]
    total_items = count_storage_items(sample_containers)
    print(total_items)