class CityCapitalLookup:
    def __init__(self):
        self.lookup_table = {
            "New York": "New York",
            "Los Angeles": "Los Angeles",
            "Chicago": "Chicago",
            "Houston": "Houston",
            "Phoenix": "Phoenix"
        }
    def get_capital(self, city_name):
        if not isinstance(city_name, str) or len(city_name.strip()) == 0:
            raise TypeError("City name must be a non-empty string")
        cleaned_city = city_name.strip()
        return self.lookup_table.get(cleaned_city, "Capital not found in the table")
if __name__ == '__main__':
    lookup_system = CityCapitalLookup()
    test_cases = [
        ("New York", True),
        ("Los Angeles", True),
        ("Chicago", True),
        (12345, False),                
        ("", False),                   
        ("Unknown City", "Capital not found in the table"),                      
    ]
    for city_input, expected_result_type in test_cases:
        try:
            result = lookup_system.get_capital(city_input)
            if isinstance(expected_result_type, bool):
                is_error = False
                if expected_result_type and not isinstance(result, str):
                    is_error = True
                elif not expected_result_type and (not isinstance(result, str)):
                    pass
            print(f"Input: {city_input!r}, Result: {result}")
        except (TypeError, KeyError) as e:
            is_error = True
            print(f"Input: {city_input!r} -> Error: {type(e).__name__}: {e}")