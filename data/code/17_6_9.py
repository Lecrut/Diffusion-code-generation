def fetch_terminal_value(sequence):
    if not sequence:
        raise ValueError("The sequence cannot be empty")
    return sequence[-1]

if __name__ == '__main__':
    test_items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    final_item = fetch_terminal_value(test_items)
    print(final_item)