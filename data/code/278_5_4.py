def item_generator(sequence):
    for item in sequence:
        yield item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    gen = item_generator(data)
    result = []
    for item in gen:
        result.append(item)
    print(result)