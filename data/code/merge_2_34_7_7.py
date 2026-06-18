from pydantic import BaseModel
class NewEntry(BaseModel):
    name: str
    age: int
    email: str
    class Config:
        extra = 'forbid'
def add_valid_entry(entries_list: list[dict], new_data: dict) -> bool:
    try:
        validated_model = NewEntry(**new_data)
        entries_list.append(validated_model.model_dump())
        return True
    except Exception:
        return False
if __name__ == '__main__':
    initial_entries = [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "Bob", "age": 25, "email": "bob@example.com"}
    ]
    test_cases = [
        {"name": "Charlie", "age": 40, "email": "charlie@test.org"},
        {"name": "", "age": 18, "email": "empty.name@bad.net"},
        {"name": "David", "age": -5, "email": "negative.age@fail.com"},
        {"name": "Eve", "age": 27, "email": ""}
    ]
    for test in test_cases:
        result = add_valid_entry(initial_entries.copy(), test)
        print(f"Entry {test}: {'Added' if result else 'Rejected'}")