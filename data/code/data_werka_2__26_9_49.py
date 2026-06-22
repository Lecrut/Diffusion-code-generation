LIST_LENGTH_THRESHOLD = 2

is_first_element_greater = lambda lst: lst[0] > lst[1] if len(lst) >= LIST_LENGTH_THRESHOLD else False

if __name__ == '__main__':
    sample_list = [7, 4]
    print(is_first_element_greater(sample_list))