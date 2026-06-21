def sorted_generator(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All items must be strings")
    
    sorted_items = sorted(items)
    for item in sorted_items:
        yield item

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    gen = sorted_generator(input_data)
    for item in gen:
        print(item, end=' ')