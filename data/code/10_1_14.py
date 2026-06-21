def get_first_element(lst):
    head, *tail = lst
    return head

if __name__ == '__main__':
    sample_list = ["red", "green", "blue", "yellow"]
    first_item = get_first_element(sample_list)
    print(first_item)