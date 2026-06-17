from pydantic import BaseModel, Field
class NewEntry(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    value: float = Field(..., ge=0.0)
def add_entry_to_dataset(entry_data: dict) -> bool:
    try:
        validated_entry = NewEntry(**entry_data)
        return True
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        {"id": 1, "name": "Alpha", "value": 5.0},
        {"id": -2, "name": "Beta", "value": 3.0},
        {"id": 3, "name": "", "value": 7.5},
        {"id": 4, "name": "Gamma", "value": -1.0}
    ]
    for case in test_cases:
        result = add_entry_to_dataset(case)
        print(f"Entry {case}: {'Added' if result else 'Rejected'}")