from dataclasses import dataclass, field
import json
from typing import List, Dict, Any
@dataclass
class DataItem:
    id: int
    name: str
    category: str
    tags: List[str] = field(default_factory=list)
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "tags": self.tags
        }
@dataclass
class DataGroup:
    group_id: int
    name: str
    items: List[DataItem] = field(default_factory=list)
    def add_item(self, item: DataItem):
        if isinstance(item, DataItem):
            self.items.append(item)
    def serialize_to_json(self) -> str:
        group_data = {
            "group_id": self.group_id,
            "name": self.name,
            "items_count": len(self.items),
            "item_details": [item.to_dict() for item in self.items]
        }
        return json.dumps(group_data)
if __name__ == '__main__':
    sample_group = DataGroup(
        group_id=101,
        name="Project Alpha Assets",
        items=[
            DataItem(id=1, name="Core Module", category="Software"),
            DataItem(id=2, name="Design Specs", category="Documentation")
        ]
    )
    sample_group.add_item(DataItem(id=3, name="API Key Config", category="Security"))
    print("Serialization Output:")
    result = sample_group.serialize_to_json()
    print(result)