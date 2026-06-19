def retrieve_first_element(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = [9, 18, 27, 36]
    print(retrieve_first_element(sample_data))