class UserRecord:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    def get_full_info(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"
class Department:
    def __init__(self, dept_id, department_name, employees=None):
        self.dept_id = dept_id
        self.department_name = department_name
        self.employees = employees if employees else []
    def get_employee_by_id(self, user_id):
        for emp in self.employees:
            if isinstance(emp, UserRecord) and emp.id == user_id:
                return emp
        raise KeyError(f"User ID {user_id} not found in department {self.department_name}")
class Organization:
    def __init__(self, org_id, organization_name):
        self.org_id = org_id
        self.organization_name = organization_name
        self.departments = {}                    
    def add_department(self, dept_obj):
        self.departments[dept_obj.dept_id] = dept_obj
def find_user_in_org(org_data, target_user_id):
    if not isinstance(org_data, Organization) or org_data.org_id is None:
        raise ValueError("Invalid organization structure")
    for dept in org_data.departments.values():
        try:
            return dept.get_employee_by_id(target_user_id)
        except KeyError as e:
            continue
    raise KeyError(f"User ID {target_user_id} not found in any department of Organization '{org_data.organization_name}'")
if __name__ == '__main__':
    emp1 = UserRecord(101, "Alice Johnson", "alice@example.com")
    emp2 = UserRecord(102, "Bob Smith", "bob@example.com")
    dept_cs = Department("D001", "Computer Science", [emp1])
    dept_math = Department("D002", "Mathematics", [])
    org_main = Organization("O001", "Tech Corp Main")
    org_main.add_department(dept_cs)
    org_main.add_department(dept_math)
    try:
        result_user = find_user_in_org(org_main, 101)
        print(result_user.get_full_info())
    except KeyError as e:
        print(f"Error: {e}")