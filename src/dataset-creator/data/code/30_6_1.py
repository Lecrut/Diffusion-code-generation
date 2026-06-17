from typing import List, Dict, Any, Union
def normalize_item(item: Union[str, int]) -> str:
    if isinstance(item, (int, float)):
        return f"num_{item}"
    elif isinstance(item, list):
        return "_".join(map(str, item))
    else:
        return str(item)
def ingest_and_normalize(data_list: List[Any]) -> Dict[str, Any]:
    normalized_data = {}
    for idx, item in enumerate(data_list):
        key = normalize_item(idx + 1)
        if isinstance(item, dict):
            value = {k: str(v) for k, v in item.items()}
        elif isinstance(item, list):
            value = [str(x) for x in item]
        else:
            value = str(item)
        normalized_data[key] = {"original": item, "processed": value}
    return normalized_data
if __name__ == '__main__':
    sample_input = [123, ["apple", 45], {"key": "value"}, "text"]
    result_dict: Dict[str, Any] = ingest_and_normalize(sample_input)
    print(result_dict)