def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_scores = [75, 82, 90, 88, 93]
    average_score = calculate_mean(sample_scores)
    print(average_score)