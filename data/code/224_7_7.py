def calculate_average(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    if count == 0:
        return None
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90]
    print(calculate_average(sample_scores))