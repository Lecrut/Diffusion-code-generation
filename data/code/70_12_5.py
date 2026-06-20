FIRST_ELEMENT = 0
LAST_ELEMENT = -1

def get_edge_elements(lst):
    return (lst[FIRST_ELEMENT], lst[LAST_ELEMENT])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_edge_elements(sample_list))