import time
from dataclasses import dataclass
@dataclass(frozen=True)
class Entity:
    id: int
    name: str
    timestamp: float
def compare_entities(entity_a: Entity, entity_b: Entity) -> dict[str, bool]:
    return {
        "id_match": entity_a.id == entity_b.id,
        "name_match": entity_a.name == entity_b.name,
        "timestamp_match": abs((entity_a.timestamp - entity_b.timestamp)) < 0.01
    }
if __name__ == '__main__':
    start_time = time.perf_counter()
    sample_entity_1 = Entity(id=42, name="Alpha", timestamp=time.time())
    sample_entity_2 = Entity(id=43, name="Beta", timestamp=time.time() + 0.5)
    result = compare_entities(sample_entity_1, sample_entity_2)
    end_time = time.perf_counter()
    print(f"Comparison Result: {result}")
    print(f"Execution Time (ms): {(end_time - start_time) * 1000:.6f}")