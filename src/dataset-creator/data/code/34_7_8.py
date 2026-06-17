from pydantic import BaseModel, Field
class NewEntry(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    value: float = Field(..., ge=0)
def add_valid_entry(dataset: list[dict], entry_data: dict[str, any]) -> bool:
    try:
        validated_entry = NewEntry(**entry_data)
        dataset.append(validated_entry.model_dump())
        return True
    except Exception:
        return False
if __name__ == '__main__':
    initial_dataset = [{"id": 1, "name": "Alpha", "value": 10.5}]
    test_cases = [
        {"id": -1, "name": "", "value": 0},
        {"id": 2, "name": "Beta", "value": -5},
        {"id": 3, "name": "Gamma", "value": 20.0}
    ]
    for case in test_cases:
        result = add_valid_entry(initial_dataset.copy(), case)
        print(f"Added entry {case}: {'Success' if result else 'Failed'}")