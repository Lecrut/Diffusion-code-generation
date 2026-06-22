def calculate_mean(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores = [10, 20, 30, 40, 50]
    mean_score = calculate_mean(scores)
    print(mean_score)