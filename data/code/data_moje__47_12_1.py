def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    examination_scores = (85, 92, 78, 90, 88)
    average_score = calculate_average(examination_scores)
    print(average_score)