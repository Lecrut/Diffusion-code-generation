def threshold_generator(threshold):
    for value in iter(int, 1):
        if value > threshold:
            yield True
if __name__ == '__main__':
    threshold_value = 10
    gen = threshold_generator(threshold_value)
    for _ in range(5):
        print(next(gen))