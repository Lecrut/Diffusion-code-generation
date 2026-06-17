import json
def sort_strings(strings: list[str], case_sensitive: bool = False) -> list[str]:
    key_func = str.lower if not case_sensitive else str
    return sorted(strings, key=key_func)
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "apple"]
    result = sort_strings(sample_data, case_sensitive=True)
    output_json = {"sorted_list": result}
    print(json.dumps(output_json))