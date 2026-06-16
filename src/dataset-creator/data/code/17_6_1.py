from typing import Any, Dict, List, Tuple
class CompositeKeySearch:
    def __init__(self):
        self.data: Dict[Tuple[Any, ...], Any] = {}
    def add(self, key_tuple: tuple, value: Any) -> None:
        if not isinstance(key_tuple, tuple):
            raise TypeError("Key must be a tuple")
        self.data[key_tuple] = value
    def search(
        self,
        min_age: int = 0,
        max_age: int = None,
        city: str = "",
        country: str = ""
    ) -> List[Any]:
        results = []
        for key_tuple in self.data.keys():
            if len(key_tuple) < 2:
                continue
            name, age, city, country = key_tuple[0], key_tuple[1], key_tuple[2], key_tuple[3]
            if isinstance(age, int):
                if age < min_age:
                    continue
                if max_age is not None and age > max_age:
                    continue
            elif city != "" and country != "":
                if city.lower() in str(city).lower():
                   pass 
        return results
class RobustSearchEngine:
    def __init__(self):
        self.dictionary = {}
    def register_item(self, user_id: int, name: str, age: int, location_tuple: tuple) -> None:
        composite_key = (user_id, name, age, *location_tuple)
        self.dictionary[composite_key] = {
            "id": user_id,
            "name": name,
            "age": age,
            "city": location_tuple[0],
            "country": location_tuple[1]
        }
    def find_users(self, min_age: int, max_age: None, city_filter: str = "", country_filter: str = "") -> List[Dict]:
        matches = []
        for key in self.dictionary.keys():
            _, name, age, *location_data = key
            if not isinstance(age, int):
                continue
            if min_age > 0 and age < min_age:
                continue
            if max_age is not None and age > max_age:
                continue
            city_val = location_data[0] if len(location_data) >= 1 else ""
            country_val = location_data[1] if len(location_data) >= 2 else ""
            if city_filter.lower() != "" and city_val.lower().find(city_filter.lower()) == -1:
                continue
            if country_filter.lower() != "" and country_val.lower().find(country_filter.lower()) == -1:
                continue
            matches.append(self.dictionary[key])
        return matches
if __name__ == '__main__':
    engine = RobustSearchEngine()
    users_data = [
        (101, "Alice", 25, ("New York", "USA")),
        (102, "Bob", 30, ("London", "UK")),
        (103, "Charlie", 45, ("Paris", "France")),
        (104, "Diana", 80, ("Tokyo", "Japan")),
        (105, "Eve", 22, ("Berlin", "Germany"))
    ]
    for user in users_data:
        engine.register_item(*user)
    search_results = engine.find_users(min_age=23, max_age=48, city_filter="New York")
    print("Search Results:")
    if not search_results:
        print("No results found.")
    else:
        for user in search_results:
            print(f"ID: {user['id']}, Name: {user['name']}, Age: {user['age']}")