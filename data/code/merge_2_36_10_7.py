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
        return self._lookup.get(normalized_city, None)
if __name__ == '__main__':
    lookup_table = CityLookup()
    test_cases = [
        "london",
        "PARIS",
        12345,
        "",
        "berlin"
    ]
    for city in test_cases:
        try:
            capital = lookup_table.get_capital(city)
            print(f"{city!r} -> {capital}")
        except TypeError as e:
            print(f"Error processing {city!r}: {e}")