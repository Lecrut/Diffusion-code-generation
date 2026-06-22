ITEM_COUNT = 10

def count_items():
    total_count = 0
    for _ in range(ITEM_COUNT):
        total_count += 1
    return total_count

if __name__ == '__main__':
    print(f"The number of items is: {count_items()}")