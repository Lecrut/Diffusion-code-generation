import numpy as np
def process_weight_data(weights):
    if len(weights) < 2:
        return []
    diff_array = np.diff(np.array(weights))
    result_list = [float(d) for d in diff_array]
    return result_list
if __name__ == '__main__':
    sample_weights = [10.5, 11.2, 9.8, 12.3, 11.7, 13.4]
    differences = process_weight_data(sample_weights)
    print(differences)