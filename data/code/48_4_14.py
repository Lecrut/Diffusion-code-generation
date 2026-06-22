def max_generator():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    def iterator():
        for item in data:
            yield item

    it = iterator()
    current_max = next(it)
    for item in it:
        if item > current_max:
            current_max = item
    return current_max

if __name__ == '__main__':
    print(max_generator())