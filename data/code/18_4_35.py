def increasing_sequence(sequence):
    PREVIOUS = 'previous'
    CURRENT = 'current'
    
    def is_increasing(prev, curr):
        return curr > prev
    
    state = {PREVIOUS: None}
    
    for value in sequence:
        if state[PREVIOUS] is not None and is_increasing(state[PREVIOUS], value):
            yield True
        else:
            yield False
        state[PREVIOUS] = value

if __name__ == '__main__':
    SAMPLE_SEQUENCE = [1, 3, 2, 5, 4, 6, 7]
    result = list(increasing_sequence(SAMPLE_SEQUENCE))
    print(result)