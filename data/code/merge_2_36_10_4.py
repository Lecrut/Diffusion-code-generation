def validate_city_name(city: str) -> bool:
    return isinstance(city, str) and len(city.strip()) > 0
CAPITALS = {
    "london": "london",
    "paris": "paris",
    "berlin": "berlin",
    "tokyo": "tokyo"
}
def lookup_city_capital(key: str) -> tuple[bool, any]:
    if not validate_city_name(key):
        return False, None
    normalized_key = key.lower().strip()
    if normalized_key in CAPITALS:
        return True, CAPITALS[normalized_key]
    else:
        return False, "City not found"
if __name__ == '__main__':
    test_cases = ["london", "Paris", 123, "", "tokyo"]
    for city in test_cases:
        is_valid, result = lookup_city_capital(city)
        if isinstance(is_valid, bool):
            print(f"Input: {repr(city)}")
            print(f"Valid: {is_valid}")
            print(f"Capital: {result}\n")