def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    average = calculate_average(scores)
    print(average)