def count_items(items):
    count = 0
    for _ in items:
        count += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"The number of items in the list is: {count_items(sample_list)}")