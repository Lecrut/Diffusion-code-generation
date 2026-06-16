import json
from dataclasses import dataclass
from typing import Any, Dict, List
@dataclass(frozen=True)
class Entity:
    id: int
    name: str
    metadata: Dict[str, Any] = None
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
def compare_entities(entity_a: Entity, entity_b: Entity) -> List[Dict[str, Any]]:
    differences = []
    id_diff = entity_a.id != entity_b.id
    name_diff = entity_a.name.lower() != entity_b.name.lower()
    metadata_diff = set(entity_a.metadata.keys()) != set(entity_b.metadata.keys()) or\
                   any(v1 != v2 for k, (v1, v2) in zip(sorted(entity_a.metadata.items()), sorted(entity_b.metadata.items())))
    if id_diff:
        differences.append({"type": "id", "entity_a_value": entity_a.id, "entity_b_value": entity_b.id})
    elif name_diff:
        differences.append({"type": "name", "entity_a_value": entity_a.name, "entity_b_value": entity_b.name})
    if metadata_diff and not id_diff and not name_diff:
        for key in sorted(set(entity_a.metadata.keys()) | set(entity_b.metadata.keys())):
            val_a = entity_a.metadata.get(key)
            val_b = entity_b.metadata.get(key)
            is_different = False
            if val_a == "None" and val_b == "None": 
                pass
            elif isinstance(val_a, str):
                if not (val_a.lower() == val_b.lower()):
                    is_different = True
            else:
                if val_a != val_b:
                    is_different = True
    return differences
if __name__ == '__main__':
    entity_1 = Entity(id=101, name="Alpha", metadata={"status": "active", "region": "US"})
    entity_2 = Entity(id=101, name="alpha", metadata={"status": "inactive", "region": "EU"})
    result = compare_entities(entity_1, entity_2)
    print(json.dumps(result))