from dataclasses import dataclass, field
from typing import List, Dict, Any
@dataclass(frozen=True)
class DataItem:
    id: int
    name: str
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "tags": self.tags.copy(),
            "metadata": self.metadata.copy()
        }
class DataOrganizer:
    def __init__(self):
        self._groups: Dict[str, List[DataItem]] = {}
    def add_item(self, item: DataItem) -> None:
        if not hasattr(item, 'tags'):
            raise TypeError("All items must have a tags attribute")
        for tag in item.tags:
            if tag not in self._groups:
                self._groups[tag] = []
            self._groups[tag].append(item)
    def get_group(self, group_name: str) -> List[DataItem]:
        return self._groups.get(group_name, [])
    def serialize_all_groups(self) -> Dict[str, Any]:
        result = {}
        for name, items in self._groups.items():
            serialized_items = [item.to_dict() for item in items]
            result[name] = {
                "count": len(items),
                "items": serialized_items
            }
        return result
if __name__ == '__main__':
    organizer = DataOrganizer()
    sample_item_1 = DataItem(id=1, name="Project Alpha", tags=["work", "urgent"], metadata={"owner": "Alice"})
    sample_item_2 = DataItem(id=2, name="Product Beta", tags=["marketing", "public"])
    sample_item_3 = DataItem(id=3, name="Internal Audit", tags=["internal", "legal"])
    organizer.add_item(sample_item_1)
    organizer.add_item(sample_item_2)
    organizer.add_item(sample_item_3)
    output = organizer.serialize_all_groups()
    print(output)