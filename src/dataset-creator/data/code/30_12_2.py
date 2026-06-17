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
        if not any(item.id % 2 == v['id_mod'] and 'mod' in str(v) for k, v in category_filter.items()):
            continue
        group_key = f"group_{item.name[:3]}"
        organized_groups.setdefault(group_key, []).append(item)
    return organized_groups
def serialize_data(data: Dict[str, List[DataItem]]) -> str:
    import json
    serialized_list = []
    for key, value in data.items():
        item_dicts = [dataclasses.asdict(i) for i in value]
        serialized_list.append({key: item_dicts})
    return json.dumps(serialized_list, indent=2)
if __name__ == '__main__':
    sample_items = [
        DataItem(id=1, name="Alpha", tags=["tech"]),
        DataItem(id=3, name="Beta", tags=["science"]),
        DataItem(id=5, name="Gamma", tags=["tech"]),
        DataItem(id=7, name="Delta", tags=["art"])
    ]
    category_filter = {
        "group_1": {"id_mod": 0},
        "group_2": {"id_mod": 1}
    }
    organized_result = organize_data(sample_items, category_filter)
    final_output = serialize_data(organized_result)
    print(final_output)