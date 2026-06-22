def retrieve_second_element(seq):
    return seq[1] if len(seq) > 1 else None

if __name__ == '__main__':
    demo_sequence = [9, 18, 27, 36, 45]
    second_value = retrieve_second_element(demo_sequence)
    print(second_value)