def average_score(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    print(average_score(sample_scores))