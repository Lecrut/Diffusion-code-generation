def safe_get(data, key, default=None):
    return data.get(key, default)
if __name__ == '__main__':
    sample_data = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print("--- Test Case 1: Key exists ---")
    name = safe_get(sample_data, "name", "Unknown")
    print(f"Retrieved name: {name}")
    print("\n--- Test Case 2: Key does not exist (using default) ---")
    occupation = safe_get(sample_data, "occupation", "No Occupation Found")
    print(f"Retrieved occupation: {occupation}")
    print("\n--- Test Case 3: Key does not exist (using None default) ---")
    country = safe_get(sample_data, "country")
    print(f"Retrieved country: {country}")
    print("\n--- Test Case 4: Retrieving a non-existent key with explicit default ---")
    zip_code = safe_get(sample_data, "zip_code", "N/A")
    print(f"Retrieved zip_code: {zip_code}")