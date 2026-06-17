class CityCapitalLookup:
    def __init__(self):
        self._lookup = {
            "New York": "Albany",
            "Los Angeles": "Sacramento",                                                                                                                                
            "Chicago": "Springfield"
        }
    def get_capital(self, city):
        if not isinstance(city, str) or len(city.strip()) == 0:
            raise TypeError("City name must be a non-empty string.")
        cleaned_city = city.strip()
        return self._lookup.get(cleaned_city, "Capital not found")
    def validate_input(self, key):
        if isinstance(key, str) and len(key) > 0:
            return True
        raise ValueError("Invalid input type or empty string.")
if __name__ == '__main__':
    lookup = CityCapitalLookup()
    test_cases = [
        "New York",
        "Los Angeles", 
        123,                                  
        "",                                   
        "Chicago"
    ]
    for city in test_cases:
        try:
            capital = lookup.get_capital(city)
            print(f"{city!r} -> {capital}")
        except (TypeError, ValueError) as e:
            print(f"Error processing {city!r}: {e}")