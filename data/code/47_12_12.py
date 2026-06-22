def calculate_average(scores):
    return sum([score for score in scores]) / len(scores)

if __name__ == '__main__':
    scores = (95, 87, 79, 92, 88, 94, 85, 76, 90, 83)
    average = calculate_average(scores)
    print(average)