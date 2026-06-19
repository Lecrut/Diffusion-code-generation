def retrieve_first_item(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(retrieve_first_item(sample_list))