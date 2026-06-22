def score_difference(scores):
    if not scores:
        return 0
    return max(scores) - min(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    print(score_difference(sample_scores))