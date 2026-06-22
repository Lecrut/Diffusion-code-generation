def calculate_average(scores):
    return sum([score for score in scores]) / len(scores)

if __name__ == '__main__':
    exam_scores = (85, 90, 78, 92, 88)
    result = calculate_average(exam_scores)
    print(result)