def average_scores(scores):
    return sum(scores.values()) / len(scores) if scores else 0

if __name__ == '__main__':
    sample_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    print(average_scores(sample_scores))