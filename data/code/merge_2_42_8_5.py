import json
def sort_strings(strings: list[str], case_sensitive: bool = False) -> dict:
    key_func = str if not case_sensitive else None
    def get_key(item):
        return item.lower() if not case_sensitive else item
    sorted_strings = sorted(strings, key=get_key)
    result = {
        "sorted_list": sorted_strings,
        "case_sensitive_used": case_sensitive
    }
    return json.dumps(result, indent=2)
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date", "Elderberry"]
    output_json = sort_strings(sample_data, case_sensitive=False)
    print(output_json)