from typing import List, Dict
class StorageContainer:
    def __init__(self, name: str) -> None:
        self.name = name
    def get_item_count(self) -> int:
        return 0
def count_items(containers: List[StorageContainer]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for container in containers:
        item_count = container.get_item_count()
        if container.name not in result:
            result[container.name] = 0
        result[container.name] += item_count
    return result
if __name__ == '__main__':
    sample_containers: List[StorageContainer] = [
        StorageContainer("Box_A"),
        StorageContainer("Crate_B"),
        StorageContainer("Pallet_C")
    ]
    aggregated_counts: Dict[str, int] = count_items(sample_containers)
    for name, total in aggregated_counts.items():
        print(f"{name}: {total}")