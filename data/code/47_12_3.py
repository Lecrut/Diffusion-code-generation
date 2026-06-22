def average_examination_scores(scores):
    total = sum([score for score in scores])
    count = len(scores)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    scores = (85, 90, 78, 92, 88, 75, 95, 82, 91, 79)
    result = average_examination_scores(scores)
    print(result)