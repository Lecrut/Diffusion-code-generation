def threshold_generator(threshold):
    first = True
    for value in iter(int, 1):
        if first:
            yield (value > threshold)
            first = False
        else:
            yield False
if __name__ == '__main__':
    threshold_value = 10
    gen = threshold_generator(threshold_value)
    for _ in range(5):
        print(next(gen))