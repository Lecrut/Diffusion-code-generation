def check_first_and_last(seq):
    if not seq:
        raise ValueError("Sequence must not be empty")
    return seq[0], seq[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    first_elem, last_elem = check_first_and_last(sample_data)
    print(first_elem, last_elem)