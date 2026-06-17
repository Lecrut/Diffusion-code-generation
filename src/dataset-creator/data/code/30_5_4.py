from dataclasses import dataclass
@dataclass(frozen=False)
class BasicObject:
    id: int
    title: str
    description: str
    status: str
    def update_title(self, new_title: str):
        self.title = new_title
    def update_description(self, new_description: str):
        self.description = new_description
    def update_status(self, new_status: str):
        self.status = new_status
if __name__ == '__main__':
    obj1 = BasicObject(id=1001, title="Project Alpha", description="Initial phase testing", status="active")
    print(f"Original Title: {obj1.title}")
    obj2 = BasicObject(id=1002, title="Beta Test", description="User feedback collection", status="pending")
    obj1.update_title("Project Alpha Revised")
    print(f"Updated Title: {obj1.title}")
    obj2.update_status("in_progress")
    print(f"New Status: {obj2.status}")