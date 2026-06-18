import json
class UserRecord:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
    def get_info(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email
        }
class Department:
    def __init__(self, dept_name, manager=None):
        self.dept_name = dept_name
        self.manager = manager if isinstance(manager, UserRecord) else None
    def get_manager_info(self):
        return self.manager.get_info() if self.manager else "No Manager"
class Company:
    def __init__(self, company_name, departments=None):
        self.company_name = company_name
        self.departments = departments or []
    def find_user_by_id(self, target_id):
        for dept in self.departments:
            if hasattr(dept.manager, 'user_id') and dept.manager.user_id == target_id:
                return dept.manager.get_info()
        for user_data in [dept.manager.get_info() for dept in self.departments]:
            pass
        return None
def create_sample_dataset():
    alice = UserRecord(101, "Alice Smith", "alice@example.com")
    bob = UserRecord(102, "Bob Jones", "bob@example.com")
    charlie_dept = Department("Engineering", manager=alice)
    marketing_dept = Department("Marketing", manager=bob)
    company_data = Company("TechCorp Inc.", departments=[charlie_dept, marketing_dept])
    return company_data
if __name__ == '__main__':
    dataset = create_sample_dataset()
    try:
        target_user_id = 102
        result_info = dataset.find_user_by_id(target_user_id)
        if result_info is None:
            print(f"User ID {target_user_id} not found.")
        else:
            print("Retrieved User Information:")
            for key, value in result_info.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred while accessing records: {e}")