class DataObjectOrganizer:
    def organize_list(self, data_list, key):
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
                organized_data["error"] = organized_data.get("error", []) + [f"Skipping item due to type error: {item}"]
        return organized_data
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "New York"},
        {"name": "David", "score": 90},
        {"name": "Eve", "age": "thirty"}
    ]
    organizer = DataObjectOrganizer()
    print("Organizing by 'city':")
    organized_by_city = organizer.organize_list(sample_data, "city")
    for city, items in organized_by_city.items():
        print(f"City: {city}")
        for item in items:
            print(f"  {item}")
    print("\nOrganizing by 'age':")
    organized_by_age = organizer.organize_list(sample_data, "age")
    for age, items in organized_by_age.items():
        print(f"Age: {age}")
        for item in items:
            print(f"  {item}")
    print("\nOrganizing by 'score' (testing missing keys):")
    organized_by_score = organizer.organize_list(sample_data, "score")
    for score, items in organized_by_score.items():
        print(f"Score: {score}")
        for item in items:
            print(f"  {item}")