def average_of_scores(scores):
    return sum([score for score in scores]) / len(scores)

if __name__ == '__main__':
    hard_coded_scores = (85, 90, 78, 92, 88)
    print(average_of_scores(hard_coded_scores))