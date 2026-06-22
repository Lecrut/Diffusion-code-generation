def compute_average(scores):
    if not scores:
        return 0.0
    total = 0.0
    for score in scores:
        total += score
    return total / len(scores)

if __name__ == '__main__':
    hardcoded_scores = [85, 90, 78, 92, 88]
    average = compute_average(hardcoded_scores)
    print(average)