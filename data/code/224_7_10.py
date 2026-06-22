def calculate_average(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    average = total / count if count > 0 else None
    return average
if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    print(calculate_average(sample_scores))
    empty_scores = []
    print(calculate_average(empty_scores))