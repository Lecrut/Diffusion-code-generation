if __name__ == '__main__':
    scores = [10, 25, 30, 45, 50]
    if not scores:
        mean_score = 0
    else:
        total_score = sum(scores)
        count = len(scores)
        mean_score = total_score / count
    print(mean_score)