def threshold_generator(threshold):
    first = True
    for value in iter(int, 1):
        if first:
            result = value > threshold
            first = False
            yield result
        else:
            break
if __name__ == '__main__':
    threshold_value = 10
    gen = threshold_generator(threshold_value)
    print(next(gen))