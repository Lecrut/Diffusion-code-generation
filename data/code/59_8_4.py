def middle_element_generator(sequence):
    n = len(sequence)
    if n == 0:
        return
    start = n // 2
    for i in range(n):
        if i == start:
            yield sequence[i]
            break
if __name__ == '__main__':
    large_sequence = list(range(1000000))
    middle_gen = middle_element_generator(large_sequence)
    result = []
    for item in middle_gen:
        result.append(item)
    print(result)