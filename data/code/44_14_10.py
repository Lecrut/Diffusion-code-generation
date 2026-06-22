def compute_average():
    scores = [85, 92, 78, 90, 88]
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

if __name__ == '__main__':
    result = compute_average()
    print(result)