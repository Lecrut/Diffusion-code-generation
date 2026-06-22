def calculate_average(scores):
    return sum([score for score in scores]) / len(scores)

if __name__ == '__main__':
    examination_scores = (95, 88, 76, 92, 85)
    result = calculate_average(examination_scores)
    print(result)