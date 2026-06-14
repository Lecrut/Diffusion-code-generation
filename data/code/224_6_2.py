import numpy as np
def calculate_mean(scores):
    np_array = np.array(scores)
    return np.mean(np_array)
if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)