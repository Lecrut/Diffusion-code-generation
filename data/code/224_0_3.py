if __name__ == '__main__':
    scores = [10, 20, 35, 40, 55]
    if not scores:
        mean_score = 0
    else:
        mean_score = sum(scores) / len(scores)
    print(mean_score)