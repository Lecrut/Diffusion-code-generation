MAX_ELEMENT_INDEX = -1

def find_max_element(sorted_list):
    return sorted_list[MAX_ELEMENT_INDEX]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 6]
    print(find_max_element(sample_list))