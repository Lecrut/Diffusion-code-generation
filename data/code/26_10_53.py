def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float.")

def threshold_generator(threshold):
    while True:
        try:
            value = yield
            validate_input(value)
            yield value > threshold
        except Exception as e:
            print(f"Error: {e}")
            yield False

if __name__ == '__main__':
    gen = threshold_generator(10)
    next(gen)
    values = [5, 15, 'a', 20, 8, 12]
    results = []
    for value in values:
        try:
            results.append(next(gen.send(value)))
        except StopIteration:
            break
    print(results)