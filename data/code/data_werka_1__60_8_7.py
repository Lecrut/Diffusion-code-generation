if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date']
    last_item_slicing = sample_strings[-1]
    last_item_indexing = sample_strings[len(sample_strings) - 1]
    print(f'List of strings: {sample_strings}')
    print(f'Last item via slicing: {last_item_slicing}')
    print(f'Last item via indexing: {last_item_indexing}')