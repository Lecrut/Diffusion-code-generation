import json
from dataclasses import dataclass
from typing import Any, Dict, List
@dataclass(frozen=True)
class Entity:
    id: int
    name: str
    value: float
    tags: List[str] = None
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
def deep_compare_entities(entity1: Entity, entity2: Entity) -> Dict[str, Any]:
    result = {
        "match": True,
        "differences": [],
        "entity1_hash": hash(json.dumps(entity1.__dict__, sort_keys=True)),
        "entity2_hash": hash(json.dumps(entity2.__dict__, sort_keys=True))
    }
    if entity1.id != entity2.id:
        result["match"] = False
        result["differences"].append({"field": "id", "value1": entity1.id, "value2": entity2.id})
    if entity1.name != entity2.name:
        result["match"] = False
        result["differences"].append({"field": "name", "value1": entity1.name, "value2": entity2.name})
    if abs(entity1.value - entity2.value) > 0.0001:
        result["match"] = False
        result["differences"].append({
            "field": "value", 
            "value1": round(entity1.value, 4), 
            "value2": round(entity2.value, 4)
        })
    if entity1.tags != entity2.tags:
        sorted_tags_1 = sorted(entity1.tags)
        sorted_tags_2 = sorted(entity2.tags)
        set_diffs = []
        for item in set(sorted_tags_1):
            if item not in sorted_tags_2:
                set_diffs.append({"type": "missing_in_entity2", "value": item})
        for item in set(sorted_tags_2):
            if item not in sorted_tags_1:
                set_diffs.append({"type": "missing_in_entity1", "value": item})
        result["differences"].extend(set_diffs)
    return result
def main():
    sample_entity_a = Entity(id=101, name="Alpha Unit", value=98.567234, tags=["active", "priority"])
    sample_entity_b = Entity(id=101, name="Beta Unit", value=98.567235, tags=["active", "critical"])
    comparison_result = deep_compare_entities(sample_entity_a, sample_entity_b)
    print(json.dumps(comparison_result, indent=4))
if __name__ == '__main__':
    main()