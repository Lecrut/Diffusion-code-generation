import json
from dataclasses import dataclass
from typing import Any, Dict, List
@dataclass
class Entity:
    id: int
    name: str
    value: float
    active: bool
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "active": self.active
        }
def compare_entities(entity_a: Entity, entity_b: Entity) -> List[Dict[str, Any]]:
    differences = []
    if entity_a.id != entity_b.id:
        differences.append({
            "field": "id",
            "entity_a_value": entity_a.id,
            "entity_b_value": entity_b.id,
            "type_mismatch": False
        })
    if entity_a.name.lower() != entity_b.name.lower():
        differences.append({
            "field": "name",
            "entity_a_value": entity_a.name,
            "entity_b_value": entity_b.name,
            "case_sensitive_match": True
        })
    abs_diff = abs(entity_a.value - entity_b.value)
    if abs_diff > 0.01:
        differences.append({
            "field": "value",
            "entity_a_value": entity_a.value,
            "entity_b_value": entity_b.value,
            "threshold_exceeded": True
        })
    if entity_a.active != entity_b.active:
        differences.append({
            "field": "active_status",
            "entity_a_value": bool(entity_a.active),
            "entity_b_value": bool(entity_b.active)
        })
    return differences
def process_batch(entities_list: List[Entity]) -> Dict[str, Any]:
    comparison_results = []
    for i in range(len(entities_list)):
        if i < len(entities_list):
            result = compare_entities(
                entities_list[i], 
                entities_list[(i + 1) % len(entities_list)]
            )
            comparison_results.append({
                "index_a": i,
                "index_b": (i + 1) % len(entities_list),
                "differences_count": len(result)
            })
    return {
        "total_pairs_compared": len(comparison_results),
        "results": comparison_results
    }
if __name__ == '__main__':
    sample_entity_1 = Entity(id=101, name="Alpha Unit", value=98.5, active=True)
    sample_entity_2 = Entity(id=101, name="alpha unit", value=97.4, active=False)
    batch_data = [sample_entity_1, sample_entity_2]
    final_output = process_batch(batch_data)
    print(json.dumps(final_output, indent=2))