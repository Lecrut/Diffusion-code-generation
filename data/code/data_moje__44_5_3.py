def compute_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    average = compute_average(scores)
    print(average)