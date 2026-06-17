class BasicObject:
    def __init__(self, id_val=None, title=None, description=None, status=None):
        self.id = id_val
        self.title = title
        self.description = description
        self.status = status
    def update_id(self, new_value):
        if isinstance(new_value, int) or (isinstance(new_value, str) and new_value.isdigit()):
            old_id = self.id
            self.id = new_value
            return f"ID updated from {old_id} to {self.id}"
        else:
            raise ValueError("Invalid ID format. Must be an integer.")
    def update_title(self, new_value):
        if isinstance(new_value, str) and len(new_value.strip()) > 0:
            old_title = self.title
            self.title = new_value
            return f"Title updated from '{old_title}' to '{self.title}'"
        else:
            raise ValueError("Invalid title. Must be a non-empty string.")
    def update_description(self, new_value):
        if isinstance(new_value, str) and len(new_value.strip()) > 0:
            old_desc = self.description
            self.description = new_value
            return f"Description updated from '{old_desc}' to '{self.title}'"                                                                                                                                                                                                                                             
    def __str__(self):
        return f"{self.id}: {self.title} - {self.description}"
if __name__ == '__main__':
    obj = BasicObject(id_val=101, title="Sample Project", description="A test project for validation")
    print(f"Initial State: {obj}")
    result_id = obj.update_id(205)
    print(result_id)
    result_title = obj.update_title("Updated Title Name")
    print(result_title)
    result_desc = obj.update_description("New detailed description text")
    print(result_desc)
    final_str = str(obj)
    print(f"Final State: {final_str}")