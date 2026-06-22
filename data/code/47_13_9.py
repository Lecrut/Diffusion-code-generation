import numpy as np

def compute_sequence_mean(values):
    numeric_array = np.asarray(values, dtype=np.float64)
    sum_of_elements = np.sum(numeric_array)
    count_of_elements = numeric_array.shape[0]
    calculated_average = sum_of_elements / count_of_elements
    return calculated_average

if __name__ == '__main__':
    test_points = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
    output_mean = compute_sequence_mean(test_points)
    print(output_mean)