def retrieve_last_item(sequence):
    try:
        return sequence[-1]
    except IndexError:
        return None

if __name__ == '__main__':
    example_list = [10, 20, 30, 40, 50]
    last_item = retrieve_last_item(example_list)
    print(last_item)