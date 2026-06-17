def count_items(collection):
    counter = 0
    for item in collection:
        counter += 1
    return counter
if __name__ == '__main__':
    sample_data = [1, 'a', True, None]
    result = count_items(sample_data)
    print(f"Total items counted: {result}")