if __name__ == '__main__':
    scores = [10, 25, 30, 45, 50]
    if not scores:
        mean_score = 0
    else:
        mean_score = sum(scores) / len(scores)
    print(mean_score)