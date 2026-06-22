def calculate_mean(scores):
    total = sum(scores)
    count = len(scores)
    mean = total / count if count != 0 else float('nan')
    return mean

if __name__ == '__main__':
    sample_scores = [82, 91, 76, 93, 85]
    result = calculate_mean(sample_scores)
    print(result)