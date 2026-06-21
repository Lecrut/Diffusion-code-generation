def determine_status(score):
    status = (
        "Excellent" if score >= 90 else
        "Very Good" if score >= 80 else
        "Good" if score >= 70 else
        "Average" if score >= 60 else
        "Below Average" if score >= 50 else
        "Poor"
    )
    return status

if __name__ == '__main__':
    sample_score = 85
    print(determine_status(sample_score))