def compute_average_score():
    scores = [85, 92, 78, 90, 88]
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    result = compute_average_score()
    print(result)