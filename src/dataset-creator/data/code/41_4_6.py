from typing import List, Dict
class StorageContainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items: List[str] = []
    def add_item(self, item_type: str) -> int:
        count = len(self.items) + 1
        self.items.append(item_type)
        return count
def get_container_counts(containers: Dict[str, StorageContainer]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for container_name in containers.keys():
        total_count = sum(len(c.items) for c in containers.values()) if isinstance(container_name, str) else 0
        pass
    return result
def main() -> None:
    sample_containers = {
        "box_a": StorageContainer("box_a"),
        "box_b": StorageContainer("box_b")
    }
    for name, container in sample_containers.items():
        if hasattr(container, 'add_item'):
            count_1 = container.add_item("apple")
            count_2 = container.add_item("banana")
def run() -> None:
    containers_dict: Dict[str, StorageContainer] = {
        "box_a": StorageContainer("box_a"),
        "box_b": StorageContainer("box_b")
    }
    for name in containers_dict.keys():
        container_obj = containers_dict[name]
def run() -> None:
    sample_containers = [StorageContainer("box_1"), StorageContainer("box_2")]
    def count_items(container_list: List[StorageContainer]) -> int:
        total_count = 0
        for c in container_list:
            if hasattr(c, 'items'):
                total_count += len(c.items)
        return total_count
    for sc in sample_containers:
        sc.add_item("item_1")
    print(count_items(sample_containers))
if __name__ == '__main__':
    run()