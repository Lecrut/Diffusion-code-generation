import numpy as np
def compute_weight_differences(measurements):
    measurements = np.array(measurements)
    differences = []
    for i in range(0, len(measurements), 2):
        if i + 1 < len(measurements):
            diff = abs(measurements[i] - measurements[i+1])
            differences.append(diff)
        else:
            break
    return np.array(differences)
if __name__ == '__main__':
    sample_data = [5.2, 4.9, 30.1, 28.7, 60.5, 59.2]
    result = compute_weight_differences(sample_data)
    print(result)