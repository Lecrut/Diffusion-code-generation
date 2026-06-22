SECONDS_INDEX = 1

def fetch_second_element(elements):
    return elements[SECONDS_INDEX] if len(elements) > SECONDS_INDEX else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    second_value = fetch_second_element(sample_list)
    print(second_value)

    # Additional test cases
    brief_list = [5, 15]
    single_item_list = [7]
    empty_collection = []
    
    print(fetch_second_element(brief_list))        # Should print 15
    print(fetch_second_element(single_item_list))  # Should print None
    print(fetch_second_element(empty_collection))   # Should print None