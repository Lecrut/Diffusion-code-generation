MAX_INDEX = -1

def find_max_element(sorted_list):
    return sorted_list[MAX_INDEX]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    print(find_max_element(sample_list))