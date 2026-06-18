import json
def sort_strings(strings: list[str], case_sensitive: bool = False) -> dict[str, str]:
    if not strings:
        return {"sorted_list": []}
    key_func = lambda x: x.lower() if not case_sensitive else x
    sorted_items = sorted(strings, key=key_func)
    return {"original_count": len(strings), "case_sensitive": case_sensitive, "sorted_list": sorted_items}
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    result = sort_strings(sample_data, case_sensitive=False)
    print(json.dumps(result))