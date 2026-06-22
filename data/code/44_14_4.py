def compute_average():
    scores = [85, 90, 78, 92, 88]
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    average = total / count
    return average

if __name__ == '__main__':
    result = compute_average()
    print(result)