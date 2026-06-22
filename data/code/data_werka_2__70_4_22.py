def get_boundary_elements(source):
    START_MARKER = 0
    END_MARKER = 1
    EMPTY_RESULT = []
    SINGLE_RESULT = []
    iterator = iter(source)
    try:
        head = next(iterator)
    except StopIteration:
        return EMPTY_RESULT
    tail = head
    index = START_MARKER
    for element in iterator:
        tail = element
        index += 1
    if index == START_MARKER:
        return SINGLE_RESULT
    return [head, tail]

if __name__ == '__main__':
    values = [10, 20, 30, 40, 50]
    print(get_boundary_elements(values))
    print(get_boundary_elements([7]))
    print(get_boundary_elements([]))