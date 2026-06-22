def calculate_mean(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")
    
    running_total = 0
    count = 0
    
    for score in scores:
        running_total += score
        count += 1
    
    return running_total / count

if __name__ == '__main__':
    sample_scores = [10, 20, 30, 40, 50]
    try:
        mean_score = calculate_mean(sample_scores)
        print(f"The mean of the scores is: {mean_score}")
    except ValueError as e:
        print(e)