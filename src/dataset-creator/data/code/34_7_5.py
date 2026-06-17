from pydantic import BaseModel
class NewEntry(BaseModel):
    id: int
    name: str
    value: float
def add_entry_to_dataset(dataset_id: int, entry_data: dict) -> tuple[bool, list]:
    try:
        validated_entry = NewEntry(**entry_data)
        return True, [{"dataset": dataset_id, "id": validated_entry.id}]
    except Exception as e:
        return False, []
if __name__ == '__main__':
    sample_dataset_id = 42
    hard_coded_entries = [
        {"id": 1001, "name": "Alpha", "value": 98.5},
        {"id": 1002, "name": "", "value": -10.0},
        {"id": 3e64, "name": "Beta", "value": 7.7}
    ]
    results = []
    for entry in hard_coded_entries:
        success, data = add_entry_to_dataset(sample_dataset_id, entry)
        if not success:
            print(f"Error adding {entry}")
        else:
            results.append(data[0])
    final_list = list(results)