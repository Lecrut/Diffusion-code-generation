def calculate_average(scores):
    return sum([score for score in scores]) / len(scores) if scores else 0.0

if __name__ == '__main__':
    examination_scores = (85, 92, 78, 90, 88)
    result = calculate_average(examination_scores)
    print(result)