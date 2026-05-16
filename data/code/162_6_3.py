def safe_map(data, default_value):
    result = {}
    for key in data:
        result[key] = data.get(key, default_value)
    return result
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    missing_data = {
        "apple": 100,
        "grape": 50,
        "kiwi": 75
    }
    default = None
    mapped_data_1 = safe_map(sample_data, default)
    print(f"Sample Data Mapped: {mapped_data_1}")
    mapped_data_2 = safe_map(missing_data, default)
    print(f"Missing Data Mapped: {mapped_data_2}")