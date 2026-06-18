class BasicObject:
    def __init__(self, id=None, title=None, description=None, status=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
    def set_id(self, new_id):
        old_id = self.id
        self.id = new_id
        return (old_id, "id")
    def set_title(self, new_title):
        old_title = self.title
        self.title = new_title
        return (old_title, "title")
    def set_description(self, new_desc):
        old_desc = self.description
        self.description = new_desc
        return (old_desc, "description")
    def set_status(self, new_status):
        old_status = self.status
        self.status = new_status
        return (old_status, "status")
if __name__ == '__main__':
    obj1 = BasicObject(id=1001, title="Sample Item", description="A test object for validation.", status="active")
    print(f"Original ID: {obj1.id}")
    old_id, attr_name = obj1.set_id(2001)
    assert attr_name == "id" and obj1.id == 2001 and obj1.title == "Sample Item"
    obj2 = BasicObject(id=3001, title="Another Object", description=None, status="pending")
    print(f"Original Title: {obj2.title}")
    old_title, attr_name = obj2.set_title("Updated Title Here")
    assert attr_name == "title" and obj2.id == 3001
    obj3 = BasicObject(id=4001)
    new_status = "completed"
    result = obj3.set_status(new_status)
    print(f"Status Update Result: {result}")
    assert obj3.status == new_status and len(result) == 2
    print("All tests passed.")