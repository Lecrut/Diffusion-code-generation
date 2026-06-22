def get_second_element(data):
    try:
        return data[1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40],
        [5],
        [],
        [100],
        [1, 2, 3]
    ]
    
    for index, lst in enumerate(sample_lists):
        print(f"List {index + 1}: {get_second_element(lst)}")