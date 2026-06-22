import numpy as np

def apply_weight_change(weights, percentage_change):
    return (np.array(weights) * (1 + percentage_change)).tolist()

if __name__ == '__main__':
    weights_list = [10.0, 20.0, 30.0]
    change_rate = 0.1
    result = apply_weight_change(weights_list, change_rate)
    print(result)