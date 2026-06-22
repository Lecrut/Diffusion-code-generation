def get_head_from_sequence(items):
    if not items:
        return None
    return items[0]

if __name__ == '__main__':
    sequence = ['alpha', 'beta', 'gamma', 'delta']
    head_element = get_head_from_sequence(sequence)
    print(head_element)
    empty_sequence = []
    head_of_empty = get_head_from_sequence(empty_sequence)
    print(head_of_empty)