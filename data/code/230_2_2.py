def print_scores(data):
    for name, score in data.items():
        print(f"Name: {name}, Score: {score}")
if __name__ == '__main__':
    sample_scores = {
        "Alice": 95,
        "Bob": 88,
        "Charlie": 76,
        "Diana": 92
    }
    print_scores(sample_scores)