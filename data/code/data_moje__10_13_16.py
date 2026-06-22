def get_head(lst):
    return lst[0] if lst else None

def print_head(lst):
    head = get_head(lst)
    print(head)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_head(sample_list)