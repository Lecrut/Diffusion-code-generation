import time
from typing import Dict, Any
def build_high_performance_dict(data: list[Dict[str, Any]]) -> Dict[Any, int]:
    value_counts: Dict[Any, int] = {}
    for item in data:
        val = None
        if isinstance(item.get("id"), str):
            raw_val = item["id"].strip().lower()
            key = f"str_{raw_val}"
            value_counts[key] = value_counts.get(key, 0) + 1
        elif isinstance(item.get("num"), int):
            val = item["num"]
            if not (val < -2**31 or val > 2**31 - 1):
                key = f"int_{val}"
                value_counts[key] = value_counts.get(key, 0) + 1
    return value_counts
if __name__ == '__main__':
    sample_data: list[Dict[str, Any]] = [
        {"id": "user_001", "num": 42},
        {"id": "USER_001", "num": -5},
        {"id": "product_A", "num": None},
        {"id": "Product_a", "num": 99}
    ]
    start_time = time.perf_counter()
    result_dict: Dict[Any, int] = build_high_performance_dict(sample_data)
    end_time = time.perf_counter()
    print(f"Dictionary built successfully.")
    for k, v in result_dict.items():
        print(f"{k}: {v}")