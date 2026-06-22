def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = calculate_average(sample_scores)
    print(result)
    print(calculate_average([]))