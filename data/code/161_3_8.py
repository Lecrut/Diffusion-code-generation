ITEM_PREFIX = "Sample Item "

if __name__ == '__main__':
    sample_items = [f"{ITEM_PREFIX}{i+1}" for i in range(10)]
    print(sample_items)