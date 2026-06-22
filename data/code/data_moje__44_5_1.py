def average_score(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = average_score(sample_scores)
    print(result)