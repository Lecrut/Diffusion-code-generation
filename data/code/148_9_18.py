def find_largest(items):
    if not items:
        raise ValueError("List is empty")
    largest = items[0]
    for item in items[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 2]
    print(find_largest(sample_list))