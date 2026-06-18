import numpy as np
def compute_weight_differences(measurements: list[list[float]]) -> float:
    if not measurements or len(measurements[0]) != 2:
        return 0.0
    diffs = []
    for old_val, new_val in measurements:
        diff = abs(new_val - old_val)
        diffs.append(diff)
    total_diff = sum(diffs)
    return float(total_diff)
if __name__ == '__main__':
    sample_data = [
        (10.5, 12.3),
        (8.7, 9.1),
        (15.0, 14.8),
        (20.2, 21.5)
    ]
    result = compute_weight_differences(sample_data)
    print(result)