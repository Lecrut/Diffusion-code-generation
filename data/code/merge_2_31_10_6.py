def match_keys_to_values(data: dict) -> list[tuple[str, int]]:
    result = []
    for key in data.keys():
        if isinstance(key, str):
            value = data[key]
            if not isinstance(value, (int, float)):
                raise TypeError(f"Value for key '{key}' must be numeric.")
            result.append((str(key), int(float(value))))
    return result
if __name__ == '__main__':
    sample_data: dict[str, str | None] = {
        "temperature": "23.5",
        "humidity": "60%",
        "pressure": "1013"
    }
    try:
        matched_pairs = match_keys_to_values(sample_data)
        print("Matched pairs:", matched_pairs)
    except TypeError as e:
        print(f"Error processing data: {e}")