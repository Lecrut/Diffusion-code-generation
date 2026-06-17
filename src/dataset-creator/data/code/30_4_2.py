import json
from dataclasses import dataclass, field
@dataclass
class User:
    id: int
    name: str = ""
    email: str = None
    def to_json(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
def serialize_objects(data_list):
    result = []
    batch_size = 1000
    processed_count = 0
    for i in range(0, len(data_list), batch_size):
        current_batch = data_list[i:i+batch_size]
        json_strings = [json.dumps(obj.to_json(), ensure_ascii=False) for obj in current_batch]
        result.append(json_string := ",".join(json_strings))
        processed_count += len(current_batch)
    return {"data": "[" + ";".join(result) + "]", "total_processed": processed_count}
if __name__ == '__main__':
    users = [User(id=1, name="Alice", email="alice@example.com"), User(id=2), User(id=3)]
    output_data = serialize_objects(users)
    print(json.dumps(output_data))