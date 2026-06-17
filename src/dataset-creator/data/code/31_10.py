import sys
def match_keys_to_values(data: dict) -> list:
    results = []
    for k, v in data.items():
        if isinstance(k, str):
            results.append((k, v))
    return results
if __name__ == '__main__':
    sample_data: dict[str, int] = {
        "alpha": 10,
        "beta": 20,
        "gamma": 30,
    }
    matched_items = match_keys_to_values(sample_data)
    for key, value in matched_items:
        print(f"{key}: {value}")