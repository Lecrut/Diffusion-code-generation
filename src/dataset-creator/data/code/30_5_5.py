class BasicObject:
    def __init__(self, id_val=None, title_val=None, description_val=None, status_val=None):
        self.id = id_val if id_val is not None else 0
        self.title = title_val if title_val is not None else ""
        self.description = description_val if description_val is not None else ""
        self.status = status_val if status_val is not None else "active"
    def update_id(self, new_value):
        self.id = new_value
    def update_title(self, new_value):
        self.title = new_value
    def update_description(self, new_value):
        self.description = new_value
    def update_status(self, new_value):
        self.status = new_value
if __name__ == '__main__':
    obj1 = BasicObject(id_val=101, title_val="Sample Project", description_val="A test project for validation.", status_val="active")
    print(f"Initial ID: {obj1.id}, Title: {obj1.title}")
    obj2 = BasicObject(title_val="Another Item", id_val=102)
    obj2.update_status("inactive")
    obj2.update_description("This item is no longer active.")
    print(f"\nUpdated Status for ID 102: {obj2.status}, Description: {obj2.description}")