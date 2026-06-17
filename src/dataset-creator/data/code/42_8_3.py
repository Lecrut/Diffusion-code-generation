import json
def sort_strings(strings: list[str], case_sensitive: bool = False) -> dict[str, any]:
    if not strings:
        return {"sorted_list": []}
    key_func = str.lower if not case_sensitive else str
    sorted_items = sorted(enumerate(strings), key=lambda x: (key_func(x[1]), x[0]))
    result = [item for _, item in sorted_items]
    return {
        "input_count": len(strings),
        "case_sensitive": case_sensitive,
        "sorted_list": result
    }
if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    output_json = sort_strings(sample_data)
    print(json.dumps(output_json))