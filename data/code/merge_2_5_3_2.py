import json
from dataclasses import dataclass
from typing import Any, Dict, List
@dataclass
class Entity:
    id: int
    name: str
    value: float
    tags: List[str]
def compare_entities(entity_a: Entity, entity_b: Entity) -> Dict[str, Any]:
    differences = []
    if entity_a.id != entity_b.id:
        differences.append({"field": "id", "a_value": entity_a.id, "b_value": entity_b.id})
    if entity_a.name.lower() != entity_b.name.lower():
        differences.append({"field": "name", "a_value": entity_a.name, "b_value": entity_b.name})
    if abs(entity_a.value - entity_b.value) > 0.01:
        differences.append({"field": "value", "a_value": entity_a.value, "b_value": entity_b.value})
    missing_in_a = set(entity_b.tags) - set(entity_a.tags)
    extra_in_a = set(entity_a.tags) - set(entity_b.tags)
    if missing_in_a or extra_in_a:
        differences.append({"field": "tags", "a_set": list(set(entity_a.tags)), "b_set": list(set(entity_b.tags))})
    return {"is_identical": len(differences) == 0, "differences": differences}
def process_batch(entities_list: List[Entity]) -> Dict[str, Any]:
    results = []
    for i in range(len(entities_list)):
        if i + 1 < len(entities_list):
            comparison_result = compare_entities(entities_list[i], entities_list[i + 1])
            results.append(comparison_result)
    return {"total_comparisons": len(results), "identical_count": sum(1 for r in results if r["is_identical"]), "results": results}
if __name__ == '__main__':
    sample_entities = [
        Entity(id=1, name="Alpha", value=98.50, tags=["active", "verified"]),
        Entity(id=2, name="Beta", value=47.30, tags=["pending"]),
        Entity(id=3, name="Gamma", value=98.50, tags=["active", "verified"]),
    ]
    batch_result = process_batch(sample_entities)
    print(json.dumps(batch_result))