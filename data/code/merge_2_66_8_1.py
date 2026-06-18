import numpy as np
def process_weights(weights: list) -> tuple[list[float], list[float]]:
    weights_array = np.array(weights)
    differences = np.diff(weights_array)
    return weights_array.tolist(), differences.tolist()
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    processed_weights, calculated_diffs = process_weights(sample_data)
    print(f"Processed Weights: {processed_weights}")
    print(f"Differences: {calculated_diffs}")