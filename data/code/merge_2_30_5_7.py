class BasicObject:
    def __init__(self, id_val=None, title=None, description=None, status=None):
        self.id = id_val if id_val is not None else 0
        self.title = title
        self.description = description
        self.status = status
    def update_id(self, new_value):
        self.id = new_value
    def update_title(self, new_value):
        self.title = new_value
    def update_description(self, new_value):
        self.description = new_value
    def update_status(self, new_value):
        self.status = new_value
if __name__ == '__main__':
    obj1 = BasicObject(id_val=101, title="Sample Project", description="A test project for validation.", status="Active")
    print(f"Initial ID: {obj1.id}")
    obj2 = BasicObject(title="Another Task", status="Pending")
    obj2.update_id(102)
    obj2.update_description("This task is pending approval.")
    print(f"\nUpdated Object 2:")
    print(f"ID: {obj2.id}, Title: {obj2.title}")