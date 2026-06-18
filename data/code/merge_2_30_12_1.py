import dataclasses
from typing import List, Dict, Any
@dataclasses.dataclass(frozen=True)
class DataItem:
    id: int
    name: str
    tags: List[str] = None
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
def organize_data(items: List[DataItem], category_filter: Dict[str, Any]) -> Dict[str, List[DataItem]]:
    organized_groups: Dict[str, List[DataItem]] = {}
    for item in items:
        if not any(item.id == cat_id and (cat_val is None or isinstance(cat_val, list) and all(isinstance(t, str) for t in cat_val)) 
                   for cat_id, cat_val in category_filter.items()):
            continue
        group_key = f"{item.name}_{category_filter.get('primary_tag', 'default')}" if item.tags else "unassigned"
        if group_key not in organized_groups:
            organized_groups[group_key] = []
        organized_groups[group_key].append(item)
    return organized_groups
def serialize_data(data_structure: Dict[str, List[DataItem]]) -> str:
    import json
    def item_to_dict(d_item):
        return {
            "id": d_item.id,
            "name": d_item.name,
            "tags": list(d_item.tags) if hasattr(d_item, 'tags') else []
        }
    serialized = {}
    for key, items in data_structure.items():
        serialized[key] = [item_to_dict(item) for item in items]
    return json.dumps(serialized, indent=2)
if __name__ == '__main__':
    sample_items: List[DataItem] = [
        DataItem(id=101, name="Alpha", tags=["urgent", "project_a"]),
        DataItem(id=102, name="Beta", tags=["review", "project_b"]),
        DataItem(id=103, name="Gamma", tags=["archived"],),
    ]
    filter_criteria: Dict[str, Any] = {
        'primary_tag': ['urgent', 'review'],
        'exclude_ids': [999],
    }
    grouped_data = organize_data(sample_items, filter_criteria)
    output_json = serialize_data(grouped_data)
    print(output_json)