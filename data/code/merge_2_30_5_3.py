class BasicObject:
    def __init__(self, obj_id: str = None, title: str = None, description: str = None, status: str = None):
        self._id = obj_id if obj_id is not None else f"obj_{len(self.__dict__.get('_objects', [])) + 1}"
        self.title = title or ""
        self.description = description or ""
        self.status = status or "active"
    def set_title(self, new_value: str):
        self.title = new_value
    def set_description(self, new_value: str):
        self.description = new_value
    def set_status(self, new_value: str):
        self.status = new_value
    def get_id(self) -> str:
        return self._id
    @property
    def id(self):
        return self.get_id()
class ObjectManager:
    _objects = []
    def add_object(self, obj: BasicObject) -> None:
        if not isinstance(obj, BasicObject):
            raise TypeError("Only instances of BasicObject can be added.")
        self._objects.append(obj)
    def get_all_objects(self) -> list:
        return self._objects.copy()
if __name__ == '__main__':
    manager = ObjectManager()
    obj1 = BasicObject(
        title="Project Alpha",
        description="A comprehensive data analysis project.",
        status="active"
    )
    obj2 = BasicObject(
        title="Beta Test",
        description=None,
        status="pending"
    )
    manager.add_object(obj1)
    manager.add_object(obj2)
    new_title = "Project Alpha Redesign"
    obj1.set_title(new_title)
    assert obj1.title == new_title and obj1.status == "active", "Title updated but status unchanged."
    print(f"Object ID: {obj1.id}")
    print(f"Updated Title: {obj1.title}")
    print(f"Status remains: {obj1.status}")