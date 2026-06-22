def calculate_mean(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [95, 88, 76, 92]
    average_score = calculate_mean(sample_scores)
    print(average_score)