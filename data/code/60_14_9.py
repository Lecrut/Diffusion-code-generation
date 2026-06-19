def fetch_last_element(array):
    if not array:
        return None
    return array[-1]

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    last_item = fetch_last_element(sample_array)
    print("The last item in the array is:", last_item)

    empty_array = []
    last_item_empty = fetch_last_element(empty_array)
    print("The last item in the empty array is:", last_item_empty)

    single_element_array = [42]
    last_item_single = fetch_last_element(single_element_array)
    print("The last item in the single element array is:", last_item_single)