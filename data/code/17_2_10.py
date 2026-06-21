def get_last_entry(sequence):
    index = len(sequence) - 1
    return sequence[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_last_entry(sample_tuple)
    print(result)