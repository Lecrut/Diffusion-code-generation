def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores_list = [85, 90, 78, 92, 88]
    result = calculate_average(scores_list)
    print(result)
    empty_result = calculate_average([])
    print(empty_result)