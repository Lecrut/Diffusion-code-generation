import json
def sort_strings(strings: list[str], case_sensitive: bool = False) -> dict:
    if not case_sensitive:
        key_func = str.lower
    else:
        key_func = str
    sorted_list = sorted(strings, key=key_func)
    return {
        "input_count": len(strings),
        "case_sensitive": case_sensitive,
        "sorted_sequence": sorted_list
    }
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    result = sort_strings(sample_data)
    print(json.dumps(result))