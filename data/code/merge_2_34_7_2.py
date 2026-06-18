from pydantic import BaseModel
class NewEntry(BaseModel):
    id: int
    name: str
    value: float
    class Config:
        extra = 'forbid'
def add_valid_entry(dataset: list[dict], entry_data: dict) -> bool:
    try:
        validated_entry = NewEntry(**entry_data)
        dataset.append(validated_entry.model_dump())
        return True
    except Exception:
        return False
if __name__ == '__main__':
    initial_dataset = [{'id': 1, 'name': 'Alpha', 'value': 10.5}]
    test_entries = [
        {'id': 2, 'name': 'Beta', 'value': 20.3},
        {'id': -1, 'name': 'Gamma', 'value': 99.9},
        {'id': 3, 'name': '', 'value': 5.0}
    ]
    results = []
    for entry in test_entries:
        is_valid = add_valid_entry(initial_dataset.copy(), entry)
        results.append(is_valid)
    print(f"Validation Results: {results}")