def get_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    test_data = [10, 20, 30]
    empty_data = []
    print(get_first_element(test_data))
    try:
        print(get_first_element(empty_data))
    except IndexError as e:
        print("Error:", e)