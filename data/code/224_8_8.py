MEAN_CALCULATION_THRESHOLD = 0

def calculate_mean(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    average_score = calculate_mean(sample_scores)
    print(average_score)