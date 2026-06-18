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
                    organized_data["unclassified"].append(item)
            except TypeError:
                organized_data["error_skipped"].append(f"Skipped item due to type error: {item}")
        return organized_data
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "New York"},
        {"name": "David", "age": 28, "city": "Chicago"},
        {"name": "Eve", "age": "thirty", "city": "Boston"}
    ]
    organizer = DataObjectOrganizer()
    print("Organizing by 'city':")
    result_by_city = organizer.organize_data(sample_data, "city")
    for city, items in result_by_city.items():
        print(f"--- {city} ({len(items)} items) ---")
        for item in items:
            print(item)
    print("\nOrganizing by 'age':")
    result_by_age = organizer.organize_data(sample_data, "age")
    for age, items in result_by_age.items():
        print(f"--- {age} ({len(items)} items) ---")
        for item in items:
            print(item)