def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores = [10, 20, 30, 40, 50]
    print(calculate_average(scores))