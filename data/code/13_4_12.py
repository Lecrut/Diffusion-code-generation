def get_nth_element(stream, n):
    for index, element in enumerate(stream):
        if index == n:
            return element
    return None

if __name__ == '__main__':
    sample_stream = (x for x in range(100))
    result = get_nth_element(sample_stream, 42)
    print(result)