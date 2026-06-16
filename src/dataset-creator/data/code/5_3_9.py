import json
from dataclasses import dataclass
from typing import Any, Dict, List
@dataclass
class Entity:
    id: int
    name: str
    value: float
    metadata: Dict[str, Any] = None
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
def compare_entities(entity_a: Entity, entity_b: Entity) -> List[Dict[str, Any]]:
    differences = []
    for attr_name in ['id', 'name', 'value']:
        val_a = getattr(entity_a, attr_name)
        val_b = getattr(entity_b, attr_name)
        if isinstance(val_a, float):
            diff_threshold = 1e-6
            is_equal = abs(float(val_a) - float(val_b)) < diff_threshold
        else:
            is_equal = (val_a == val_b)
        if not is_equal:
            differences.append({
                'attribute': attr_name,
                'entity_a_value': val_a,
                'entity_b_value': val_b,
                'is_different': True
            })
    metadata_diffs = []
    for key in set(entity_a.metadata.keys()) | set(entity_b.metadata.keys()):
        val_a = entity_a.metadata.get(key)
        val_b = entity_b.metadata.get(key)
        if isinstance(val_a, float):
            diff_threshold = 1e-6
            is_equal = abs(float(val_a) - float(val_b)) < diff_threshold
        else:
            is_equal = (val_a == val_b)
        if not is_equal or key in entity_a.metadata ^ key in entity_b.metadata:
            metadata_diffs.append({
                'attribute': f'metadata.{key}',
                'entity_a_value': str(val_a),
                'entity_b_value': str(val_b),
                'is_different': True
            })
    return differences
def serialize_comparison(comparison_result: List[Dict[str, Any]]) -> str:
    if not comparison_result:
        return json.dumps({'status': 'identical', 'details': []})
    else:
        result_data = {
            'status': 'different',
            'differences': [item for item in comparison_result]
        }
        return json.dumps(result_data)
if __name__ == '__main__':
    entity_1 = Entity(id=101, name="Alpha", value=98.567432, metadata={"source": "db_a"})
    entity_2 = Entity(id=101, name="Beta", value=98.567435, metadata={"source": "db_b"})
    result_list = compare_entities(entity_1, entity_2)
    output_string = serialize_comparison(result_list)
    print(output_string)