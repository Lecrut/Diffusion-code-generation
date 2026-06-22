def get_last_entry(sequence):
    iterator = iter(sequence)
    last = None
    for item in iterator:
        last = item
    return last

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_last_entry(sample_tuple)
    print(result)