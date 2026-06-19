def threshold_generator(threshold):
    first = True
    for value in iter(int, 1):
        if first:
            first = False
            yield (value > threshold)
        else:
            break
if __name__ == '__main__':
    threshold_value = 50
    gen = threshold_generator(threshold_value)
    print(next(gen))
    try:
        print(next(gen))
    except StopIteration:
        print(False)