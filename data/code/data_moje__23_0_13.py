def calculate_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric type.")
    if math.isnan(score) or math.isinf(score):
        raise ValueError("Score cannot be NaN or infinity.")
    if score < 0:
        raise ValueError("Score cannot be negative.")
    if score > 100:
        raise ValueError("Score cannot exceed 100.")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

import math

if __name__ == '__main__':
    scores = [100, 95, 85, 75, 65, 50, 0]
    for s in scores:
        print(calculate_grade(s))