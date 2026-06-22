def average_of_scores():
    scores = [85, 92, 78, 95, 88, 76, 90, 82, 94, 86]
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    result = average_of_scores()
    print(result)