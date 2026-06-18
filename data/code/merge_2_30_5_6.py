class BasicObject:
    def __init__(self, id_val: str = "", title: str = "", description: str = "", status: int = 0):
        self._id = id_val
        self._title = title
        self._description = description
        self._status = status
    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, value: str):
        self._title = value
    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def status(self) -> int:
        return self._status
    @status.setter
    def status(self, value: int):
        self._status = value
    def update_id(self, new_id: str):
        self._id = new_id
    def update_title(self, new_title: str):
        self._title = new_title
    def update_description(self, new_desc: str):
        self._description = new_desc
    def update_status(self, new_status: int):
        self._status = new_status
if __name__ == '__main__':
    obj1 = BasicObject(id_val="001", title="Project Alpha", description="A critical system upgrade.", status=1)
    print(f"Initial ID: {obj1.id}, Title: {obj1.title}")
    obj2 = BasicObject(id_val="002", title="Beta Test", description="", status=-1)
    obj1.update_title("Project Alpha Redesign")
    print(f"Updated ID: {obj1.id}, Updated Title: {obj1.title}")
    obj2.update_description("Testing phase only.")
    print(f"Obj 2 Description: {obj2.description}, Status remains: {obj2.status}")