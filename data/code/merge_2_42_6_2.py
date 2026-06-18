from typing import List
class CustomObject:
    def __init__(self, name: str) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f"CustomObject(name={self.name!r})"
def sort_custom_objects(objects: List[CustomObject]) -> List[CustomObject]:
    if not all(isinstance(obj, CustomObject) for obj in objects):
        raise TypeError("All elements must be instances of CustomObject.")
    return sorted(objects, key=lambda x: (x.name is None, str(x.name)))
if __name__ == '__main__':
    sample_objects = [
        CustomObject(name="Charlie"),
        CustomObject(name=None),
        CustomObject(name="Alpha"),
        CustomObject(name="Beta"),
        CustomObject(name=12345)                                                                                                                                                          
    ]
    sorted_objects = sort_custom_objects(sample_objects)
    for obj in sorted_objects:
        print(obj.name)