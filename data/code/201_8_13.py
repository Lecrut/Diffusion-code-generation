def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores = {
        'A': 85,
        'B': 92,
        'C': 78,
        'D': 90
    }
    average_score = calculate_average(scores.values())
    print(f"Average score: {average_score:.2f}")