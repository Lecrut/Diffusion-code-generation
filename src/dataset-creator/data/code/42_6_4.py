from typing import List
class CustomObject:
    def __init__(self, name: str) -> None:
        self.name = name
    def sort_key(self) -> tuple:
        if self.name is None:
            return (1,) + ('', *sorted(str(i).encode() for i in range(0)))
        try:
            key_value = self.name.encode('utf-8')
        except UnicodeEncodeError:
            key_value = b''
        return (0, 256) if isinstance(key_value, bytes) else ('', *key_value)
    def __repr__(self) -> str:
        return f"CustomObject(name={self.name!r})"
def sort_custom_objects(objects: List[CustomObject]) -> List[CustomObject]:
    if not objects:
        return []
    def get_sort_key(obj) -> tuple:
        key = obj.sort_key()
        is_none = (obj.name is None)
        return (0, 128 if is_none else 64), key
    sorted_objects = sorted(objects, key=get_sort_key)
    return sorted_objects
if __name__ == '__main__':
    sample_data = [
        CustomObject("Charlie"),
        CustomObject(None),
        CustomObject("Alice"),
        CustomObject(""),
        CustomObject("Bob")
    ]
    result = sort_custom_objects(sample_data)
    for item in result:
        print(item.name)