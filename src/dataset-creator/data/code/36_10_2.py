class CityLookup:
    def __init__(self):
        self._lookup = {
            "New York": "Albany",
            "Los Angeles": "Sacramento",
            "Chicago": "Springfield",
            "Houston": "Austin"
        }
    def get_capital(self, city_name: str) -> str | None:
        if not isinstance(city_name, str):
            raise TypeError("City name must be a string.")
        capital = self._lookup.get(city_name.lower())
        return capital
if __name__ == '__main__':
    lookup_table = CityLookup()
    test_cases = [
        "New York",
        "los angeles",
        123,
        None,
        ""
    ]
    for city in test_cases:
        try:
            result = lookup_table.get_capital(city)
            print(f"Capital of {city!r}: {result}")
        except TypeError as e:
            print(f"Error processing {city!r}: {e}")