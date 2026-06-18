from typing import List
class CustomObject:
    def __init__(self, name: str) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f"CustomObject(name={self.name!r})"
def sort_custom_objects(objects: List[CustomObject]) -> List[CustomObject]:
    return sorted(objects, key=lambda obj: (obj.name is None, str(obj.name)))
if __name__ == '__main__':
    sample_objects = [
        CustomObject("Charlie"),
        CustomObject(None),
        CustomObject("Alice"),
        CustomObject("Bob"),
        CustomObject(""),
        CustomObject("Zoe")
    ]
    sorted_objects = sort_custom_objects(sample_objects)
    for obj in sorted_objects:
        print(obj.name)