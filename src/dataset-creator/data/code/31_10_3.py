import sys
def match_keys_to_values(data: dict) -> list:
    results = []
    for k in data.keys():
        if isinstance(k, int):
            results.append((k, data[k]))
    return results
if __name__ == '__main__':
    sample_data: dict[int, str] = {101: "Alice", 202: "Bob"}
    matched_items = match_keys_to_values(sample_data)
    for item in matched_items:
        print(item[0], "=", item[1])