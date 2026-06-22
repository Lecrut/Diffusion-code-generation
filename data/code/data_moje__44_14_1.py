def compute_average_score():
    scores = [85, 90, 78, 92, 88]
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    print(compute_average_score())