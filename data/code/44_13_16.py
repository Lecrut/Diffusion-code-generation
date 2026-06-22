SCORE_MAPPING = {
    "math": 88,
    "science": 92,
    "history": 75,
    "english": 85,
}

def compute_average(results: dict) -> float:
    if not results:
        return 0.0
    values = list(results.values())
    return sum(values) / len(values)

if __name__ == '__main__':
    scores = {
        "math": 95,
        "science": 88,
        "history": 79,
        "english": 91,
    }
    average = compute_average(scores)
    print(average)