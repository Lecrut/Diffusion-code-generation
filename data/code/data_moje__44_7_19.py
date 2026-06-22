def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    count = len(scores)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    average = calculate_average(scores)
    print(average)