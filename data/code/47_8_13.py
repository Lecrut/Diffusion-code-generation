def calculate_mean(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if len(scores) == 0:
        raise ValueError("List cannot be empty")
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    mean_score = calculate_mean(sample_scores)
    print(mean_score)
    
    mixed_scores = [85, 90, 'invalid', 92, 88]
    try:
        calculate_mean(mixed_scores)
    except TypeError as e:
        print("TypeError caught:", str(e))
    
    try:
        calculate_mean([])
    except ValueError as e:
        print("ValueError caught:", str(e))