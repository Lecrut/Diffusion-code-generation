class CityLookup:
    def __init__(self):
        self._lookup = {
            "New York": "New York",
            "Los Angeles": "Los Angeles",
            "Chicago": "Chicago",
            "Houston": "Houston",
            "Phoenix": "Phoenix"
        }
    @staticmethod
    def validate_key(key):
        if not isinstance(key, str) or key.strip() == "":
            raise TypeError("City name must be a non-empty string.")
    def get_capital(self, city_name: str) -> str | None:
        self.validate_key(city_name)
        return self._lookup.get(city_name.lower())
if __name__ == '__main__':
    lookup = CityLookup()
    test_cases = [
        "New York",
        "chicago",
        123,
        "",
        None
    ]
    for city in test_cases:
        try:
            capital = lookup.get_capital(city)
            print(f"{city!r} -> {capital}")
        except Exception as e:
            print(f"Error processing {city!r}: {e}")