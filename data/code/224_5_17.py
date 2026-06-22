def mean_generator(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
        yield (total / count)
if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    mean_gen = mean_generator(sample_scores)
    print(next(mean_gen))
    for _ in range(1, len(sample_scores)):
        print(next(mean_gen))