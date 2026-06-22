def nth_element(stream, n):
    for index, value in enumerate(stream):
        if index == n:
            return value
    raise IndexError(f"Index {n} is out of range for the stream")

if __name__ == "__main__":
    def sample_generator():
        yield 10
        yield 20
        yield 30
        yield 40
        yield 50

    result = nth_element(sample_generator(), 2)
    print(result)