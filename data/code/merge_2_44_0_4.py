class UserDatabase:
    def __init__(self):
        self.data = {
            "users": [
                {"id": 101, "name": "Alice", "role": ["admin", "editor"], "departments": [{"dept_id": 501, "title": "Manager"}, {"dept_id": 502, "title": "Intern"}]},
                {"id": 102, "name": "Bob", "role": ["viewer"], "departments": []},
                {"id": 103, "name": "Charlie", "role": ["editor"], "departments": [{"dept_id": 503, "title": "Lead"}]}
            ]
        }
    def find_user_by_role(self, target_role):
        for user in self.data["users"]:
            if any(target_role in role_list for role_list in user.get("role", [])):
                return {"id": user["id"], "name": user["name"]}
        raise KeyError(f"User with role '{target_role}' not found")
    def get_user_department_titles(self, user_id):
        target = None
        try:
            for u in self.data["users"]:
                if u["id"] == user_id:
                    target = u
                    break
        except IndexError:
            raise KeyError("User ID not found")
        departments_list = []
        dept_info = target.get("departments", [])
        for i, dept in enumerate(dept_info):
            try:
                if isinstance(dept, dict) and "title" in dept:
                    title = dept["title"]
                    if len(title) > 0:
                        departments_list.append({"index": i, "department_id": dept.get("dept_id"), "title": title})
            except TypeError:
                continue
        return departments_list
    def get_all_admins(self):
        admins = []
        for user in self.data["users"]:
            if any(role == "admin" for role in user.get("role", [])):
                admins.append(user)
        return admins
if __name__ == '__main__':
    db = UserDatabase()
    try:
        alice_info = db.find_user_by_role("editor")
        dept_titles = None
        if "id" in alice_info and isinstance(alice_info.get("departments"), list):
            for i, d in enumerate(db.data["users"]):
                if d["id"] == alice_info["id"]:
                    dept_titles = db.get_user_department_titles(d["id"])
                    break
    except Exception as e:
        print(f"Error occurred: {e}")