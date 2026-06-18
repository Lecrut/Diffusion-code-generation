import pprint
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "New York"},
    {"name": "David", "age": 28, "city": "Chicago"},
    {"name": "Eve", "age": 22, "city": "Los Angeles"}
]
organized_data = {
    "New York": {},
    "Los Angeles": {},
    "Chicago": {}
}
for item in data:
    city = item["city"]
    if city in organized_data:
        organized_data[city][item["name"]] = item
    else:
        new_city_group = {
            "name": item["name"],
            "age": item["age"],
            "city": city
        }
        organized_data[city] = {
            "group": [new_city_group]
        }
if __name__ == '__main__':
    pprint.pprint(organized_data)