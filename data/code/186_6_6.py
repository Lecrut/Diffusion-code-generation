def sorted_generator(items):
    for item in sorted(items):
        yield item

if __name__ == '__main__':
    large_list = ["cherry", "apple", "elderberry", "banana", "date"]
    sorted_items = sorted_generator(large_list)
    print(" ".join(sorted_items))