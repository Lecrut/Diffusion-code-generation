from typing import List, Dict
class StorageContainer:
    def __init__(self, name: str, item_count: int):
        self.name = name
        self.item_count = item_count
def get_container_counts(containers: List[StorageContainer]) -> Dict[str, int]:
    return {container.name: container.item_count for container in containers}
if __name__ == '__main__':
    sample_containers: List[StorageContainer] = [
        StorageContainer("Box_A", 10),
        StorageContainer("Bin_B", 25),
        StorageContainer("Pallet_C", 42)
    ]
    aggregated_data: Dict[str, int] = get_container_counts(sample_containers)
    print(aggregated_data)