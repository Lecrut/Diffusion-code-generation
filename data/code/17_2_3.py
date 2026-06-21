def get_last_entry(sequence):
    last = None
    for item in sequence:
        last = item
    return last

sample_tuple = (1, 2, 3, 4, 5)

if __name__ == '__main__':
    result = get_last_entry(sample_tuple)
    print(result)