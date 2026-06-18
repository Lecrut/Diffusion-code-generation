class SafeDictionaryAccess:
    def __init__(self, data):
        self.data = data if isinstance(data, dict) else {}
    def get_nested_value(self, path_parts):
        try:
            current = self.data
            for part in path_parts:
                if isinstance(current, dict):
                    current = current.get(part)
                else:
                    break
            return current
        except Exception as e:
            print(f"Error accessing nested data: {e}")
            raise
def create_sample_dataset():
    return {
        "company": {
            "name": "Acme Corp",
            "departments": [
                {"id": 1, "name": "Engineering"},
                {"id": 2, "name": "Marketing"}
            ]
        },
        "employees": {
            "count": 450,
            "active_workers": {
                "seniority_levels": ["Junior", "Senior"]
            }
        },
        "location": None                                               
    }
def main():
    dataset = create_sample_dataset()
    accessor = SafeDictionaryAccess(dataset)
    company_name = accessor.get_nested_value(["company", "name"])
    print(f"Company Name: {company_name}")
    location_info = accessor.get_nested_value(["location", "city"])
    if location_info is not None:
        print(f"Location City: {location_info}")
    else:
        print("No specific city data available.")
    try:
        first_dept = accessor.get_nested_value(["company", "departments", "0"])
        if isinstance(first_dept, dict):
            dept_name = first_dept.get("name")
            print(f"First Department Name: {dept_name}")
    except IndexError:
        print("Error accessing department index.")
if __name__ == '__main__':
    main()