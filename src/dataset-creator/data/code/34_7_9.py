from pydantic import BaseModel, Field
class NewEntry(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    value: float = Field(..., ge=0)
def add_entry_to_dataset(entry_data: dict[str, any]) -> bool:
    try:
        validated_entry = NewEntry(**entry_data)
        return True
    except Exception:
        return False
if __name__ == '__main__':
    valid_input = {"id": 10, "name": "Test Item", "value": 5.5}
    invalid_id = {"id": -5, "name": "Bad ID", "value": 2.0}
    result_valid = add_entry_to_dataset(valid_input)
    print(f"Valid entry added: {result_valid}")
    result_invalid = add_entry_to_dataset(invalid_id)
    print(f"Invalid entry rejected: {not result_invalid}")