def print_scores(data):
    for name, score in data.items():
        print(f"Name: {name}, Score: {score}")
if __name__ == '__main__':
    scores = {
        "Alice": 95,
        "Bob": 88,
        "Charlie": 92,
        "David": 79
    }
    print_scores(scores)