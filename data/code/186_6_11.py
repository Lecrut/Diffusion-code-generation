def sorted_generator(items):
    for item in sorted(items):
        yield item

if __name__ == '__main__':
    items = ["banana", "apple", "cherry", "date", "elderberry"]
    gen = sorted_generator(items)
    for item in gen:
        print(item, end=' ')