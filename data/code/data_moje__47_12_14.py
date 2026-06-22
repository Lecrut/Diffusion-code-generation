def average_scores(scores):
    return sum([s for s in scores]) / len(scores)

if __name__ == '__main__':
    scores = (85, 90, 78, 92, 88)
    result = average_scores(scores)
    print(result)