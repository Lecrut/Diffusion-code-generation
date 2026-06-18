import json
def sort_strings(strings: list[str], case_sensitive: bool = False) -> dict:
    if not case_sensitive:
        key_func = str.lower
    else:
        key_func = str
    return {
        "sorted_list": sorted(strings, key=key_func),
        "case_sensitivity_enabled": True if case_sensitive else False
    }
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    result_case_insensitive = sort_strings(sample_data)
    result_case_sensitive = sort_strings(sample_data, case_sensitive=True)
    output_json = {
        "case_insensitive": result_case_insensitive["sorted_list"],
        "case_sensitive": result_case_sensitive["sorted_list"],
        "metadata": {"input_count": len(sample_data)}
    }
    print(json.dumps(output_json))