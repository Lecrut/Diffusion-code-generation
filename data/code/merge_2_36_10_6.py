class CityLookup:
    def __init__(self):
        self._lookup = {
            "london": "london",
            "paris": "paris",
            "berlin": "berlin",
            "moscow": "moscow",
            "tokyo": "tokyo"
        }
    def get_capital(self, city):
        if not isinstance(city, str) or len(city.strip()) == 0:
            raise TypeError("City name must be a non-empty string.")
        normalized_city = city.lower().strip()
        if normalized_city in self._lookup:
            return self._lookup[normalized_city]
        else:
            raise KeyError(f"Unknown city: {city}")
if __name__ == '__main__':
    lookup_table = CityLookup()
    test_cases = [
        ("london", "London"),
        ("Paris", "Paris"),
        ("berlin", "Berlin"),
        ("unknown_city", None),                      
        (123, None)                                   
    ]
    for city_name in test_cases:
        try:
            capital = lookup_table.get_capital(city_name[0]) if isinstance(city_name, tuple) else lookup_table.get_capital(city_name)
            print(f"City: {city_name}, Capital: {capital}")
        except (KeyError, TypeError) as e:
            print(f"Error for input '{city_name}': {e}")