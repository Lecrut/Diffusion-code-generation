from typing import List, Dict
class StorageContainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items_count: int = 0
    def add_items(self, count: int) -> None:
        if not isinstance(count, (int, float)):
            raise TypeError("Count must be numeric.")
        self.items_count += int(round(count))
def get_container_counts(containers: List[StorageContainer]) -> Dict[str, int]:
    return {container.name: container.items_count for container in containers}
if __name__ == '__main__':
    container_a = StorageContainer("Alpha")
    container_b = StorageContainer("Beta")
    container_a.add_items(150)
    container_b.add_items(75.3)                                                
    results: Dict[str, int] = get_container_counts([container_a, container_b])
    print(results)