def middle_element_generator(sequence):
    n = len(sequence)
    if n == 0:
        return
    start_index = (n - 1) // 2
    for i in range(start_index, start_index + 1):
        yield sequence[i]
if __name__ == '__main__':
    large_sequence = list(range(1000000))
    print("Middle element of the large sequence:")
    for element in middle_element_generator(large_sequence):
        print(element)