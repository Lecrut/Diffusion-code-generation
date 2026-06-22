def retrieve_first_element(seq):
    return seq[0] if seq else None

if __name__ == '__main__':
    example_list = [10, 20, 30, 40]
    print(retrieve_first_element(example_list))