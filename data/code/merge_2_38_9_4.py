def memory_efficient_iterator():
    for i in range(10):
        yield f"key_{i}", str(i * 2)
if __name__ == '__main__':
    result = {}
    iterator = memory_efficient_iterator()
    while True:
        try:
            key, value = next(iterator)
            result[key] = value
        except StopIteration:
            break
    print(result)