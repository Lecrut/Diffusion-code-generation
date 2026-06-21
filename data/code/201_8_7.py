def calculate_average(scores):
    if not scores:
        return None
    total = sum(scores.values())
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    student_scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'David': 90
    }
    print(f"Average score: {calculate_average(student_scores)}")