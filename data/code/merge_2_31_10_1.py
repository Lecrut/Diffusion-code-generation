from typing import Any, Dict, List
def match_keys_to_values(data: Dict[str, Any]) -> List[tuple]:
    results = []
    for key in data.keys():
        if not isinstance(key, str):
            continue
        value = data[key]
        try:
            parsed_value = float(value)
            if 0 <= parsed_value <= 100:
                results.append((key, round(parsed_value, 2)))
        except (ValueError, TypeError):
            pass
    return results
if __name__ == '__main__':
    sample_data = {
        "score_a": "85.5",
        "score_b": "invalid",
        "percentage_c": "90",
        "count_d": 123,
        "ratio_e": "0.75"
    }
    matched_pairs = match_keys_to_values(sample_data)
    print(matched_pairs)