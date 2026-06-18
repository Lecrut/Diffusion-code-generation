class DataObjectOrganizer:
    def organize_data(self, data_list, key):
        organized_data = {}
        for item in data_list:
            try:
                if key in item:
                    category = item[key]
                    if category not in organized_data:
                        organized_data[category] = []
                    organized_data[category].append(item)
                else:
                    organized_data["unassigned"] = organized_data.get("unassigned", []) + [item]
            except TypeError:
                organized_data["error_skipped"] = organized_data.get("error_skipped", []) + [item]
        return organized_data
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "New York"},
        {"name": "David", "occupation": "Engineer"},
        {"name": "Eve", "age": "thirty"},
        {"name": "Frank", "age": 40, "city": "Los Angeles"}
    ]
    organizer = DataObjectOrganizer()
    print("Organizing by 'city':")
    organized_by_city = organizer.organize_data(sample_data, "city")
    for city, items in organized_by_city.items():
        print(f"City: {city}")
        for item in items:
            print(f"  {item}")
    print("\nOrganizing by 'age':")
    organized_by_age = organizer.organize_data(sample_data, "age")
    for age, items in organized_by_age.items():
        print(f"Age: {age}")
        for item in items:
            print(f"  {item}")
    print("\nOrganizing by 'occupation':")
    organized_by_occupation = organizer.organize_data(sample_data, "occupation")
    for occupation, items in organized_by_occupation.items():
        print(f"Occupation: {occupation}")
        for item in items:
            print(f"  {item}")