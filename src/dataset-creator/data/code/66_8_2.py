import numpy as np
def process_weight_data(weights):
    return weights - weights.mean(axis=0)
if __name__ == '__main__':
    data = np.array([123456789, 234567890, 345678901])
    result = process_weight_data(data)
    print(result)