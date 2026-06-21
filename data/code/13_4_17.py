def get_nth_element(stream, n):
    for index, value in enumerate(stream):
        if index == n:
            return value
    raise IndexError("Index out of range")

if __name__ == "__main__":
    sample_generator = (x * 2 for x in range(10))
    result = get_nth_element(sample_generator, 5)
    print(result)