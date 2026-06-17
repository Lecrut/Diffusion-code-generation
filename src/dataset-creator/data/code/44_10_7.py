def safe_get(data: dict, *keys) -> any:
    current = data
    if not isinstance(current, dict):
        raise TypeError(f"Expected a dictionary, got {type(current).__name__}")
    for key in keys:
        try:
            next_level = current[key]
        except KeyError:
            return None
        if not isinstance(next_level, dict):
            return None
        current = next_level
    return current
if __name__ == '__main__':
    SAMPLE_DATA: dict = {
        "country": {
            "capital": "Paris",
            "currency": {"code": "EUR", "symbol": "$"}
        },
        "population": 6700000,
        "flags": ["france.png"]
    }
    result_1 = safe_get(SAMPLE_DATA, "country", "capital")
    result_2 = safe_get(SAMPLE_DATA, "country", "currency", "code")
    result_3 = safe_get(SAMPLE_DATA, "missing_key")
    result_4 = safe_get(SAMPLE_DATA, "country", "region")
    print(f"Capital: {result_1}")
    print(f"Currency Code: {result_2}")
    print(f"Missing Top Key Result: {result_3}")
    print(f"Non-existent Sub-key Result: {result_4}")