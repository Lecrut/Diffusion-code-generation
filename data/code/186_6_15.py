def sorted_generator(items):
    items.sort()
    for item in items:
        yield item

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_items = sorted_generator(input_data)
    print(*sorted_items)