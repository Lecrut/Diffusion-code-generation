def compute_mean(scores):
    if not all(isinstance(score, (int, float)) for score in scores):
        raise ValueError("All elements in scores must be numbers")
    
    running_total = 0
    count = 0
    
    for score in scores:
        running_total += score
        count += 1
    
    if count == 0:
        raise ValueError("Scores list cannot be empty")
    
    return running_total / count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    try:
        mean_score = compute_mean(sample_scores)
        print(f"Mean score: {mean_score}")
    except ValueError as e:
        print(e)