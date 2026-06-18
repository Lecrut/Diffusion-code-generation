import time
from dataclasses import dataclass
@dataclass(frozen=True)
class Entity:
    id: int
    name: str
    timestamp: float
    metadata: dict = None
def compare_entities(entity_a: Entity, entity_b: Entity) -> list[str]:
    differences = []
    if entity_a.id != entity_b.id:
        differences.append(f"ID mismatch: {entity_a.id} vs {entity_b.id}")
    if entity_a.name.lower() != entity_b.name.lower():
        differences.append("Name case-insensitive mismatch")
    time_diff = abs(entity_a.timestamp - entity_b.timestamp)
    if time_diff > 0.1:
        differences.append(f"Timestamp drift detected: {time_diff:.4f}s")
    if entity_a.metadata != entity_b.metadata:
        for key in set((entity_a.metadata or {}).keys() | (entity_b.metadata or {}).keys()):
            val_a = entity_a.metadata.get(key) if entity_a.metadata else None
            val_b = entity_b.metadata.get(key) if entity_b.metadata else None
            if val_a != val_b:
                differences.append(f"Metadata key '{key}' differs")
    return differences
if __name__ == '__main__':
    sample_entity_1 = Entity(id=42, name="Alpha Unit", timestamp=time.time(), metadata={"status": "active"})
    sample_entity_2 = Entity(id=43, name="alpha unit", timestamp=time.time() + 0.5, metadata={"status": "inactive"})
    start_time = time.perf_counter_ns()
    result = compare_entities(sample_entity_1, sample_entity_2)
    end_time = time.perf_counter_ns()
    print("Comparison Results:")
    for diff in result:
        print(diff)
    elapsed_ms = (end_time - start_time) / 1e6
    print(f"Execution Time: {elapsed_ms:.4f} ms")