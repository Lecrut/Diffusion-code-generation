def average_scores(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

if __name__ == '__main__':
    print(average_scores([85, 90, 78, 92, 88]))
    print(average_scores([]))