def calculate_average(scores):
    if not scores:
        return None
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    print(calculate_average(sample_scores))
    print(calculate_average([]))
    print(calculate_average([100]))
    print(calculate_average([50, 60, 70]))