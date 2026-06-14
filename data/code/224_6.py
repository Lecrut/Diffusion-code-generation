import numpy as np
def calculate_mean(scores):
    np_array = np.array(scores)
    return np.mean(np_array)
if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)