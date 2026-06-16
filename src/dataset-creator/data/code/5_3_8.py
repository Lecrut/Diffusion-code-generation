import time
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class Entity:
    id: int
    name: str
    value: float
def calculate_difference(entity1: Entity, entity2: Entity) -> dict[str, bool]:
    return {
        "id_match": entity1.id == entity2.id,
        "name_match": entity1.name.lower() == entity2.name.lower(),
        "value_match": abs(entity1.value - entity2.value) < 0.001,
        "entity_equal": (entity1.id == entity2.id and 
                        entity1.name == entity2.name and 
                        entity1.value == entity2.value),
    }
def compare_entities_real_time(e1: Entity, e2: Entity) -> tuple[bool, dict[str, bool]]:
    start = time.perf_counter_ns()
    result = calculate_difference(e1, e2)
    end = time.perf_counter_ns()
    latency_ms = (end - start) / 1_000_000
    is_identical = all(result.values())
    return is_identical, {**result, "latency_ms": round(latency_ms, 6)}
if __name__ == '__main__':
    sample_entity_a = Entity(id=42, name="Alpha", value=10.5)
    sample_entity_b = Entity(id=42, name="alpha", value=10.501)
    is_same, details = compare_entities_real_time(sample_entity_a, sample_entity_b)
    print(f"Entities match: {is_same}")
    for key, val in details.items():
        if isinstance(val, bool):
            print(f"{key}: {val}")
        else:
            print(f"{key}: {val}")