def find_first_element(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [99]
    sample_list_3 = []
    print(f"First element of {sample_list_1}: {find_first_element(sample_list_1)}")
    print(f"First element of {sample_list_2}: {find_first_element(sample_list_2)}")
    try:
        print(f"First element of {sample_list_3}: {find_first_element(sample_list_3)}")
    except IndexError as e:
        print(f"Error for {sample_list_3}: {e}")