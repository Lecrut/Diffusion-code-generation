from pydantic import BaseModel, Field
class NewEntry(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    value: float = Field(..., ge=0)
def add_entry_to_dataset(entry_data: dict[str, any]) -> None:
    validated_entry = NewEntry(**entry_data)
    dataset_id_list.append(validated_entry.id)
if __name__ == '__main__':
    global dataset_id_list
    dataset_id_list = []
    sample_entries = [
        {"id": 1, "name": "Alpha", "value": 10.5},
        {"id": -2, "name": "Beta", "value": 20.0},
        {"id": 3, "name": "", "value": 30.0}
    ]
    for entry in sample_entries:
        try:
            add_entry_to_dataset(entry)
            print(f"Added ID {entry['id']}")
        except Exception as e:
            print(f"Validation failed for {entry}: {e}")