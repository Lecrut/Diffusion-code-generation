if __name__ == '__main__':
    SAMPLE_LIST = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    LAST_ITEM_SLICING = SAMPLE_LIST[-1]
    LAST_ITEM_INDEXING = SAMPLE_LIST[len(SAMPLE_LIST) - 1]
    print(f'List: {SAMPLE_LIST}')
    print(f'Last element via slicing: {LAST_ITEM_SLICING}')
    print(f'Last element via indexing: {LAST_ITEM_INDEXING}')
    MOST_EFFICIENT_METHOD = LAST_ITEM_SLICING
    print(f'Most efficient solution: {MOST_EFFICIENT_METHOD}')