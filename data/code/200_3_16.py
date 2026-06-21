def extract_keys(data_list, keys):
    return [{key: item[key] for key in keys if key in item} for item in data_list]

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Apple", "category": "Fruit"},
        {"id": 2, "name": "Banana", "category": "Fruit"},
        {"id": 3, "name": "Carrot", "category": "Vegetable"}
    ]
    keys_to_extract = ["id", "name"]
    extracted_data = extract_keys(sample_data, keys_to_extract)
    print(extracted_data)