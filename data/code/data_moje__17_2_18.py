def get_last_entry(sequence):
    last_item = None
    for item in sequence:
        last_item = item
    return last_item

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_last_entry(sample_tuple)
    print(result)