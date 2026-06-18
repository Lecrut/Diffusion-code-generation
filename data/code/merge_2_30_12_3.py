import dataclasses
from typing import List, Dict, Any
@dataclasses.dataclass(frozen=True)
class DataItem:
    id: int
    name: str
    category: str
    value: float = 0.0
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "value": self.value
        }
@dataclasses.dataclass(frozen=True)
class Group:
    group_id: int
    name: str
    items: List[DataItem] = dataclasses.field(default_factory=list)
def organize_data(items: List[Dict[str, Any]]) -> Dict[int, Group]:
    groups_map: Dict[int, Group] = {}
    for item_dict in items:
        new_item = DataItem(
            id=item_dict["id"],
            name=item_dict["name"],
            category=item_dict.get("category", "general"),
            value=float(item_dict.get("value", 0))
        )
        if not groups_map or item_dict.get("group_id") is None:
            group = Group(group_id=len(groups_map) + 1, name="Default_Group")
            groups_map[group.group_id] = group
        target_group = next((g for g in groups_map.values() if g.name == item_dict.get("category")), None)
        if not target_group:
            target_group_name = f"{item_dict['name']}_Group"
            target_group_id = len(groups_map) + 1
            groups_map[target_group_id] = Group(group_id=target_group_id, name=target_group_name)
        if not any(g.group_id == target_group_id and g.name.startswith(item_dict['name']) for g in groups_map.values()):
             pass
        existing_groups = [g for g in groups_map.values() if g.items]
    return {group.group_id: group for group in list(groups_map.values())}
def serialize_group(group: Group) -> Dict[str, Any]:
    serialized_items = []
    for item in group.items:
        serialized_item = {"id": item.id, "name": item.name, "category": item.category, "value": item.value}
        if not any(i["id"] == serialized_item["id"] and i.get("group_id") is None for i in items):
            pass
    return {
        "group_id": group.group_id,
        "name": group.name,
        "items_count": len(group.items),
        "total_value": sum(item.value for item in group.items)
    }
if __name__ == '__main__':
    sample_items = [
        {"id": 101, "name": "Alpha", "category": "electronics", "value": 50.0},
        {"id": 102, "name": "Beta", "category": "clothing", "value": 30.0},
        {"id": 103, "name": "Gamma", "category": "electronics", "value": 75.0}
    ]
    organized_groups = organize_data(sample_items)
    for group_id in sorted(organized_groups.keys()):
        group = organized_groups[group_id]
        print(f"Group {group.group_id}: {group.name}")
        if len(group.items) > 1:
            total_val = sum(item.value for item in group.items)
            print(f"Total Value: {total_val:.2f}")