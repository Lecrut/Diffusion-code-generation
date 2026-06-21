def get_middle_element(data):
    if len(data) == 0:
        raise ValueError("Sequence is empty")
    return data[len(data) // 2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(get_middle_element(sample_tuple))
    print(get_middle_element((1, 2, 3)))
    try:
        print(get_middle_element(()))
    except ValueError:
        print("Caught expected error for empty tuple")