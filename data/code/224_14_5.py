def calculate_mean(scores):
    total = sum(scores)
    count = len(scores)
    mean = total / count if count != 0 else float('nan')
    return mean

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(sample_scores)
    print(result)