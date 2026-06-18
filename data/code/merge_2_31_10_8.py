import sys
def match_keys_to_values(data: dict) -> list:
    results = []
    for k in data.keys():
        if isinstance(k, str):
            v = data[k]
            if not isinstance(v, int):
                continue
            results.append((k, v))
    return results
if __name__ == '__main__':
    sample_data: dict[str, any] = {
        "alpha": 10,
        "beta": None,
        "gamma": -5.2,
        "delta": True,
        "epsilon": 42,
    }
    matched_pairs = match_keys_to_values(sample_data)
    for k, v in matched_pairs:
        print(f"{k}: {v}")