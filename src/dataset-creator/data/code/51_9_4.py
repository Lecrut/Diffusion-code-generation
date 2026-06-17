import timeit
def find_initial_entry_optimized(data):
    return data[0] if len(data) > 0 else None
if __name__ == '__main__':
    sample_data = [1, 'apple', True, {'key': 'value'}, "final"]
    result = find_initial_entry_optimized(sample_data)
    if isinstance(result, list):
        print("List is empty.")
    else:
        print(f"Initial entry found: {result}")