class BasicObject:
    def __init__(self, id_val=None, title=None, description=None, status=None):
        self.id = id_val if id_val is not None else 0
        self.title = title if title is not None else ""
        self.description = description if description is not None else ""
        self.status = status if status is not None else "active"
    def update_id(self, new_id):
        self.id = new_id
    def update_title(self, new_title):
        self.title = new_title
    def update_description(self, new_desc):
        self.description = new_desc
    def update_status(self, new_status):
        self.status = new_status
if __name__ == '__main__':
    obj1 = BasicObject(id_val=101, title="Sample Project", description="A test project for validation.", status="active")
    print(f"Initial ID: {obj1.id}, Title: {obj1.title}")
    obj2 = BasicObject(title="Another Item", status="inactive")
    obj1.update_id(102)
    obj2.update_title("Updated Another Item")
    obj2.update_status("pending")
    print(f"Modified ID: {obj1.id}, Modified Title: {obj2.title}")