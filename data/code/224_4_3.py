def compute_average(data):
    if not data:
        raise ValueError("No scores provided")
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores = (95, 88, 76, 90, 85)
    result = compute_average(sample_scores)
    print(result)