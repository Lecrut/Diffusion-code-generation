def mean_scores(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    
    total = 0
    count = 0
    
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements in the list must be numeric")
        total += score
        count += 1
    
    if count == 0:
        raise ValueError("List must not be empty")
    
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 95, 88]
    result = mean_scores(sample_scores)
    print(result)