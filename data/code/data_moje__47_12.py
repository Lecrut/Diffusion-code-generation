def calculate_average(scores):
    return sum([score for score in scores]) / len(scores)

if __name__ == '__main__':
    examination_scores = (85, 90, 78, 92, 88)
    result = calculate_average(examination_scores)
    print(result)