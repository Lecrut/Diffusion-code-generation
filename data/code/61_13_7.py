def fetch_element(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    SAMPLE_TUPLE = (10, 20, 30, 40, 50)
    SAMPLE_LIST = ['a', 'b', 'c', 'd', 'e']
    
    INDEX_TO_FETCH = 2
    
    print(fetch_element(SAMPLE_TUPLE, INDEX_TO_FETCH))
    print(fetch_element(SAMPLE_LIST, INDEX_TO_FETCH))