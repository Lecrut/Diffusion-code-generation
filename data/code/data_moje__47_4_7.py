import math

def calculate_mean(results):
    return math.fsum(results) / len(results)

if __name__ == '__main__':
    scores = [10.0, 20.0, 30.0, 40.0, 50.0]
    average = calculate_mean(scores)
    print(average)