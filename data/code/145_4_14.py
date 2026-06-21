def determine_status(score):
    if score < 0:
        return "Invalid"
    elif score >= 90:
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
    sample_scores = [95, 85, 75, 65, 55, -1]
    for score in sample_scores:
        print(f"Score: {score}, Status: {determine_status(score)}")