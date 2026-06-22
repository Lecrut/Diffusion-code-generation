def mean_of_scores(scores):
    if not scores:
        raise ValueError("Input sequence is empty")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = (85, 90, 78, 92)
    print(mean_of_scores(sample_scores))