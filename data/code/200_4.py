def calculate_total_score(data):
    total_score = 0
    for name, score in data:
        total_score += score
    return total_score
if __name__ == '__main__':
    scores_data = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    total = calculate_total_score(scores_data)
    print(total)