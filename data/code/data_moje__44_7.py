def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    avg = calculate_average(sample_scores)
    print(avg)