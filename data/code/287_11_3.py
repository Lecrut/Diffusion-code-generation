import numpy as np
def convert_weights(raw_weights):
    if not raw_weights:
        return []
    converted_weights = []
    for weight in raw_weights:
        if isinstance(weight, (int, float)):
            converted_weights.append(weight / 1000.0)
        else:
            try:
                converted_weights.append(float(weight))
            except ValueError:
                converted_weights.append(np.nan)
    return converted_weights
if __name__ == '__main__':
    raw_data = [1500, 2500, 3000, 4000]
    def convert_weights_lc(raw_weights):
        return [w / 1000.0 for w in raw_weights]
    result_lc = convert_weights_lc(raw_data)
    print(f"List Comprehension Result: {result_lc}")
    np_data = np.array(raw_data)
    result_np = np_data / 1000.0
    print(f"NumPy Result: {result_np}")