def calculate_average(scores):
    if not scores:
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

if __name__ == '__main__':
    print(calculate_average([85, 90, 78, 92, 88]))
    print(calculate_average([]))
    print(calculate_average([100]))
    print(calculate_average([50, 50, 50]))