from typing import Any, Dict
def build_high_performance_dict(data: list[tuple[Any, ...]]) -> dict[str, int]:
    result = {}
    for item in data:
        key = str(item[0]) if isinstance(item[0], (int, float)) else repr(item[0])
        value = 1 + result.get(key, 0)
        result[key] = value
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple",), ("banana",), ("cherry",), 
        ("apple",), ("date",), ("elderberry",), 
        ("fig",), ("grape",), ("honeydew",)
    ] * 100_000
    dictionary = build_high_performance_dict(sample_data)
    print(f"Processed {len(dictionary)} unique entries.")