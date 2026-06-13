def calculate_total_score(data):
    total = 0
    for name, score in data:
        total += score
    return total
if __name__ == '__main__':
    scores_data = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 95)
    ]
    total_score = calculate_total_score(scores_data)
    print(total_score)