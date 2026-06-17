from pydantic import BaseModel
class NewEntry(BaseModel):
    id: int
    name: str
    value: float
def add_valid_entry(dataset_list: list[dict], entry_data: dict) -> bool:
    try:
        validated = NewEntry(**entry_data)
        dataset_list.append(validated.model_dump())
        return True
    except Exception:
        return False
if __name__ == '__main__':
    sample_dataset = [{'id': 1, 'name': 'Item A', 'value': 10.5}]
    test_entry = {'id': 2, 'name': 'New Item', 'value': 20.0}
    result = add_valid_entry(sample_dataset.copy(), test_entry)
    print(f"Entry added: {result}")