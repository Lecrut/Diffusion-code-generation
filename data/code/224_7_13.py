def calculate_average(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92]
    print(calculate_average(sample_scores))