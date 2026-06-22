def calculate_average(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    result = calculate_average(scores)
    print(result)
    
    empty_scores = []
    empty_result = calculate_average(empty_scores)
    print(empty_result)