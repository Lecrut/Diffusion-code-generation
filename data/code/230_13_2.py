def print_scores(data):
    for name, score in data.items():
        print(f"{name}: {score}")
if __name__ == '__main__':
    scores = {
        "Alice": 95,
        "Bob": 88,
        "Charlie": 76,
        "David": 92
    }
    print_scores(scores)