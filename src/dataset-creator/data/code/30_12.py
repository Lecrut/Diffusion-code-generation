from dataclasses import dataclass, field
import json
from typing import List, Dict, Any
@dataclass(frozen=True)
class DataItem:
    id: int
    name: str
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "tags": self.tags,
            "metadata": self.metadata
        }
class DataOrganizer:
    def __init__(self):
        self._groups: Dict[str, List[DataItem]] = {}
    def add_item(self, item: DataItem) -> None:
        if not isinstance(item, DataItem):
            raise TypeError("Only DataItem instances can be added.")
        group_key = f"{item.name}_{item.id}"
        self._groups.setdefault(group_key, []).append(item)
    def get_group(self, key: str) -> List[DataItem]:
        return self._groups.get(key, [])
    def serialize_all_groups(self) -> Dict[str, Any]:
        result = {}
        for group_name in sorted(self._groups.keys()):
            items = [item.to_dict() for item in self._groups[group_name]]
            result[group_name] = {
                "count": len(items),
                "items": items
            }
        return result
if __name__ == '__main__':
    organizer = DataOrganizer()
    sample_items = [
        DataItem(id=1, name="Project Alpha", tags=["dev"], metadata={"version": 2.0}),
        DataItem(id=2, name="Project Beta", tags=["prod"], metadata={"status": "active"}),
        DataItem(id=3, name="Project Alpha", tags=["qa"], metadata={})
    ]
    for item in sample_items:
        organizer.add_item(item)
    serialized_data = organizer.serialize_all_groups()
    print(json.dumps(serialized_data, indent=2))