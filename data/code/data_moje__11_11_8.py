def pop_last_safe(sequence):
    EMPTY_SENTINEL = []
    if sequence == EMPTY_SENTINEL or len(sequence) == 0:
        return None
    return sequence.pop()

if __name__ == '__main__':
    NON_EMPTY_DATA = [100, 200, 300]
    print(pop_last_safe(NON_EMPTY_DATA))
    print(NON_EMPTY_DATA)
    
    EMPTY_DATA = []
    print(pop_last_safe(EMPTY_DATA))
    
    SINGLE_ITEM_DATA = [42]
    print(pop_last_safe(SINGLE_ITEM_DATA))
    print(SINGLE_ITEM_DATA)