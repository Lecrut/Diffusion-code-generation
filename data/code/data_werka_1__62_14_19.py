def retrieve_second_element(data):
    return data[1] if len(data) >= 2 else None

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40],
        [5],
        [],
        [100],
        [1, 2]
    ]

    for idx, lst in enumerate(sample_lists):
        print(f"List {idx + 1}: Second element is {retrieve_second_element(lst)}")