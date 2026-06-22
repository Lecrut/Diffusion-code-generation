def threshold_generator(threshold):
    first = True
    for value in iter(range(10)):
        if first:
            first = False
            if value > threshold:
                yield True
            else:
                yield False
        else:
            yield value
if __name__ == '__main__':
    threshold_value = 5
    gen = threshold_generator(threshold_value)
    for result in gen:
        print(result)