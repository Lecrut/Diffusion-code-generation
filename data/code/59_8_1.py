def middle_element_generator(sequence):
    n = len(sequence)
    if n == 0:
        return
    middle_index = n // 2
    yield sequence[middle_index]
if __name__ == '__main__':
    large_sequence = list(range(1000000))
    print("Middle element of the large sequence:")
    for element in middle_element_generator(large_sequence):
        print(element)