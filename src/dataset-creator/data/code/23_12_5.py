from typing import Dict, Any, List
class ItemRegistry:
    def __init__(self):
        self._data: Dict[str, Dict[str, Any]] = {}
    def add_item(self, name: str, metadata: Dict[str, Any]) -> None:
        if not isinstance(name, str) or not isinstance(metadata, dict):
            raise TypeError("Name must be a string and metadata must be a dictionary.")
        self._data[name] = metadata
    def get_item(self, name: str) -> Dict[str, Any]:
        return self._data.get(name, {})
    def list_items(self) -> List[tuple]:
        return sorted(self._data.items())
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_data = [
        ("apple", {"color": "red", "calories": 52}),
        ("banana", {"color": "yellow", "calories": 89}),
        ("cherry", {"color": "dark red", "calories": 41})
    ]
    for name, meta in sample_data:
        registry.add_item(name, meta)
    print("Registered items:")
    for item_name, details in registry.list_items():
        print(f"{item_name}: {details}")
    retrieved = registry.get_item("banana")
    if "color" in retrieved and "calories" in retrieved:
        print(f"\nRetrieved banana data successfully.")