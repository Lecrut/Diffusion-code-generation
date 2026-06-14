if __name__ == '__main__':
    scores = [10, 20, 30, 40, 50]
    if not scores:
        mean = 0
    else:
        mean = sum(scores) / len(scores)
    print(mean)