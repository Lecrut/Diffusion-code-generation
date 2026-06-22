import math

def calculate_mean(results):
    if not results:
        return 0.0
    total = math.fsum(results)
    return total / len(results)

if __name__ == '__main__':
    scores = [98.1, 85.5, 92.3, 76.8, 89.4]
    average = calculate_mean(scores)
    print(average)