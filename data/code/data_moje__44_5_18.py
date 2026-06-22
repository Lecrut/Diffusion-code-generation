def compute_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 95, 88]
    average = compute_average(sample_scores)
    print(average)