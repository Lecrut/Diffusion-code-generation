from typing import List
class CustomObject:
    def __init__(self, name: str) -> None:
        self.name = name
    @property
    def display_name(self) -> str:
        return self.name if self.name is not None else ""
def sort_objects(objects: List[CustomObject]) -> List[CustomObject]:
    return sorted(
        objects, key=lambda obj: (obj.display_name.lower(), id(obj))
    )
if __name__ == '__main__':
    sample_data = [
        CustomObject("Zebra"),
        None,                                                                                           
        CustomObject(""),
        CustomObject("apple"),
        CustomObject(None),
        CustomObject("Banana")
    ]
    safe_objects = [obj for obj in sample_data if isinstance(obj, CustomObject)]
    sorted_list = sort_objects(safe_objects)
    print("Sorted Objects:")
    for item in sorted_list:
        name_value = getattr(item, 'name', "Unknown") or ""
        print(f"Name: '{name_value}' | Display Name: {item.display_name}")