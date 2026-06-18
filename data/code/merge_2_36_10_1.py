class CityLookup:
    def __init__(self):
        self._lookup = {
            "New York": "Albany",
            "Los Angeles": "Sacramento",
            "Chicago": "Springfield"
        }
    def get_capital(self, city_name: str) -> str | None:
        if not isinstance(city_name, str):
            raise TypeError("City name must be a string.")
        return self._lookup.get(city_name.lower())
if __name__ == '__main__':
    lookup = CityLookup()
    test_cases = ["New York", "los angeles", 12345, None]
    for city in test_cases:
        try:
            capital = lookup.get_capital(city)
            print(f"{city!r} -> {capital}")
        except Exception as e:
            print(f"Error processing {city!r}: {e}")