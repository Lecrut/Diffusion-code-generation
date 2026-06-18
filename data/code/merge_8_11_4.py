import numpy as np
def compare_data_sets(data1, data2):
    np1 = np.array(data1)
    np2 = np.array(data2)
    mean1 = np.mean(np1)
    mean2 = np.mean(np2)
    var1 = np.var(np1)
    var2 = np.var(np2)
    return {
        "mean_difference": mean1 - mean2,
        "variance_difference": var1 - var2
    }
if __name__ == '__main__':
    set_a = [1.0, 2.0, 3.0, 4.0, 5.0]
    set_b = [6.0, 7.0, 8.0, 9.0, 10.0]
    results = compare_data_sets(set_a, set_b)
    print(results)