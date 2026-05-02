def get_first_element(data_list):
    if not data_list:
        return None
    return data_list[0]
if __name__ == '__main__':
    sample1 = [10, 20, 30]
    sample2 = ['a', 'b', 'c']
    sample3 = []
    sample4 = [42]
    print(f"First element of {sample1}: {get_first_element(sample1)}")
    print(f"First element of {sample2}: {get_first_element(sample2)}")
    print(f"First element of {sample3}: {get_first_element(sample3)}")
    print(f"First element of {sample4}: {get_first_element(sample4)}")