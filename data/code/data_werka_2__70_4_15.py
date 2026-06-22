def extract_ends(iterable):
    result_list = []
    current_first = None
    last_seen = None
    count_processed = 0
    for element in iterable:
        if count_processed == 0:
            current_first = element
        last_seen = element
        count_processed += 1
    if count_processed == 0:
        result_list = []
    elif count_processed == 1:
        result_list = [current_first]
    else:
        result_list = [current_first, last_seen]
    return result_list

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25, 30]
    extracted = extract_ends(numbers)
    print(extracted)
    single_element = extract_ends([99])
    print(single_element)
    empty_list = extract_ends([])
    print(empty_list)