def threshold_generator(threshold):
    for value in range(100):
        if value > threshold:
            yield True
        else:
            yield False
if __name__ == '__main__':
    threshold_value = 50
    gen = threshold_generator(threshold_value)
    for result in gen:
        print(result)