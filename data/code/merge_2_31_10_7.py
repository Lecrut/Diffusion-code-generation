import sys
def match_keys_to_values(data: dict) -> list:
    results = []
    for key in data.keys():
        if not isinstance(key, str):
            continue
        value = data[key]
        if isinstance(value, (int, float)):
            results.append((key, f"{value}"))
        elif isinstance(value, list) and len(value) > 0:
            items_str = ", ".join(str(item) for item in value[:3]) + ("..." if len(value) > 3 else "")
            results.append((key, f"[{items_str}]"))
    return results
if __name__ == '__main__':
    sample_data = {
        "temperature": 25.5,
        "humidity": [60, 70],
        "status": True,
        "invalid_key_123": None,
        "pressure": {"unit": "hPa", "value": 1013}
    }
    matched_results = match_keys_to_values(sample_data)
    print("Key-Value Matches:")
    for key, value in matched_results:
        print(f"{key}: {value}")