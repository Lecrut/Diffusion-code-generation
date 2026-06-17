from typing import List, Dict
def count_storage_items(containers: List[Dict[str, int]]) -> int:
    return sum(container.get("item_count", 0) for container in containers)
if __name__ == '__main__':
    sample_containers = [
        {"id": "container_1", "item_count": 5},
        {"id": "container_2", "item_count": 3},
        {"id": "container_3", "item_count": 7}
    ]
    total_items = count_storage_items(sample_containers)
    print(total_items)