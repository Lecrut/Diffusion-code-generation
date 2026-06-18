import json
def sort_strings(strings: list[str], case_sensitive: bool = True) -> list[str]:
    if not strings:
        return []
    key_func = str.lower if not case_sensitive else str
    sorted_list = sorted(strings, key=key_func)
    return sorted_list
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "apple", "Banana"]
    result = sort_strings(sample_data, case_sensitive=False)
    output_json = json.dumps(result)
    print(output_json)