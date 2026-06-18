def get_nested_value(data: dict, *keys) -> object | None:
    current: dict | None = data
    for key in keys:
        if not isinstance(current, dict):
            return None
        try:
            current = current[key]
        except KeyError:
            return None
    return current
def main():
    hierarchy_data = {
        "company": {
            "name": "TechCorp",
            "departments": {
                "engineering": {"lead": "John Doe", "projects": ["Alpha", "Beta"]},
                "marketing": {"lead": "Jane Smith"}
            }
        },
        "location": {
            "city": "San Francisco"
        }
    }
    result_1 = get_nested_value(hierarchy_data, "company", "departments", "engineering", "lead")
    print(f"Engineering Lead: {result_1}")
    result_2 = get_nested_value(hierarchy_data, "non_existent_key")
    print(f"Non-existent Top Key Result: {result_2}")
    result_3 = get_nested_value(hierarchy_data, "company", "departments", "engineering", "nonexistent_project")
    print(f"Non-existent Project Result: {result_3}")
    result_4 = get_nested_value(hierarchy_data, "location", "city")
    print(f"City Name: {result_4}")
    result_5 = get_nested_value(hierarchy_data, "company", "city")
    print(f"Company City Path Result: {result_5}")
if __name__ == '__main__':
    main()