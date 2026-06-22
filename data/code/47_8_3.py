def calculate_mean(scores):
    if not scores:
        raise ValueError("List is empty")
    total = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError(f"Non-numeric element found: {score}")
        total += score
    return total / len(scores)

if __name__ == '__main__':
    scores_list = [85, 90, 78, 92, 88]
    result = calculate_mean(scores_list)
    print(result)