def compute_mean(values: list[float]) -> float:
    total = 0.0
    count = 0
    for number in values:
        total += number
        count += 1
    return total / count if count > 0 else 0.0

DATA_SETS: dict[str, list[float]] = {
    "set_a": [12.4, 15.8, 9.2, 22.1, 18.5],
    "set_b": [5.0, 5.0, 5.0, 5.0],
    "set_c": [0.1, 0.2, 0.3, 0.4, 0.5]
}

if __name__ == '__main__':
    target_key = "set_a"
    if target_key in DATA_SETS:
        sample_values = DATA_SETS[target_key]
        result = compute_mean(sample_values)
        print(result)