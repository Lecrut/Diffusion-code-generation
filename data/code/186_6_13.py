def sorted_generator(items):
    sorted_items = sorted(items)
    for item in sorted_items:
        yield item

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    sorter = sorted_generator(input_data)
    print(*sorter)