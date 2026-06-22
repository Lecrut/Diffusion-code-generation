def get_first_element(seq):
    if len(seq) == 0:
        raise IndexError("The sequence is empty.")
    return seq[0]

if __name__ == '__main__':
    print(get_first_element([10, 20, 30]))
    print(get_first_element((4, 5, 6)))
    print(get_first_element([9]))