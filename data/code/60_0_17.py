def retrieve_last_element(sequence):
    if not sequence:
        return None
    return sequence[-1]

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    last_item = retrieve_last_element(example_list)
    print(last_item)