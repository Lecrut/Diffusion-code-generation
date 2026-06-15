import numpy as np
def calculate_mean(score_list):
    score_array = np.array(score_list)
    return np.mean(score_array)
if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)