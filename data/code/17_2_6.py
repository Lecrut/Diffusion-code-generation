def get_last_entry(sequence):
    result = None
    for item in sequence:
        result = item
    return result

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(get_last_entry(sample_tuple))