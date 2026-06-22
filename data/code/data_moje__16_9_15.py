DEFAULT_EMPTY_RESULT = None

def get_first_element(items):
    if len(items) == 0:
        return DEFAULT_EMPTY_RESULT
    head = items[0]
    return head

if __name__ == '__main__':
    sample_input = [100, 200, 300]
    empty_input = []
    print(get_first_element(sample_input))
    print(get_first_element(empty_input))