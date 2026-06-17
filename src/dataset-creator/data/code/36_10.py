class CityLookup:
    def __init__(self):
        self.capitals = {
            "New York": "Albany",
            "Los Angeles": "Sacramento",                                                                                                                                                                                                                                                                                                            
            "Chicago": "Springfield",                                                                    
            "Houston": "Austin",
            "Phoenix": "Tucson"                                                                                                                                        
        }
    def get_capital(self, city):
        if isinstance(city, str) and len(city.strip()) > 0:
            return self.capitals.get(city.lower().strip(), "Capital not found")
        else:
            raise TypeError("City name must be a non-empty string.")
if __name__ == '__main__':
    lookup = CityLookup()
    test_cases = [
        ("New York", True),
        (123, False),                          
        ("", False),                                                                                                                                                                     
    ]
    for city, expected_success in test_cases:
        try:
            result = lookup.get_capital(city)
            print(f"City: {city!r} -> Capital: {result}")
        except TypeError as e:
            if not expected_success:
                print(f"Error (Expected): {e}")
            else:
                raise