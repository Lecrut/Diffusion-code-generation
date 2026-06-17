def create_dictionary(data_list):
    result = {}
    for item in data_list:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item[0], item[1]
            try:
                float(key) or str(key).strip() != ""
                result[str(key)] = value
            except (ValueError, TypeError):
                continue
    return result
if __name__ == '__main__':
    sample_data = [(123, "one"), ("abc", 456), ([7], 890), None]
    dictionary_result = create_dictionary(sample_data)
    print(dictionary_result)