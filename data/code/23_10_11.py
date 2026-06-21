def score_to_grade(score: int) -> str:
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    test_scores = [95, 82, 70, 55, 0, 100]
    for s in test_scores:
        result = score_to_grade(s)
        print(f"Score: {s}, Grade: {result}")