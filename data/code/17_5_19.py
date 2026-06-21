DEFAULT_EMPTY_INDICATOR = "__EMPTY__"

def retrieve_last_element(sequence, empty_indicator=DEFAULT_EMPTY_INDICATOR):
    if len(sequence) == 0:
        return empty_indicator
    return sequence[-1]

if __name__ == '__main__':
    sample_list = ["alpha", "bravo", "charlie", "delta"]
    result = retrieve_last_element(sample_list)
    print(result)
    
    empty_list = []
    empty_result = retrieve_last_element(empty_list)
    print(empty_result)