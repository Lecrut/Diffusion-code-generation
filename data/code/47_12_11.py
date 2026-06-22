def calculate_average(scores):
    return sum([score for score in scores]) / len(scores)

if __name__ == '__main__':
    hard_coded_scores = (85, 92, 78, 90, 88, 95, 82, 89, 91, 87)
    average = calculate_average(hard_coded_scores)
    print(average)