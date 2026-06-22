def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    average = calculate_average(scores)
    print(average)