def mean_generator(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
        yield total / count

scores = [85, 92, 78, 90, 88, 94, 86, 93, 89, 91]

if __name__ == '__main__':
    mean_gen = mean_generator(scores)
    for _ in range(len(scores)):
        print(next(mean_gen))