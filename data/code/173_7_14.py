from collections import defaultdict
from typing import List, NamedTuple

class Item(NamedTuple):
    category: str
    value: int

def group_by_field(namedtuples: List[NamedTuple], field_name: str) -> dict:
    grouped = defaultdict(list)
    for item in namedtuples:
        key = getattr(item, field_name)
        grouped[key].append(item)
    return dict(grouped)

if __name__ == '__main__':
    items = [
        Item('fruit', 10),
        Item('vegetable', 5),
        Item('fruit', 20),
        Item('grain', 30),
        Item('vegetable', 15)
    ]
    grouped_items = group_by_field(items, 'category')
    print(grouped_items)