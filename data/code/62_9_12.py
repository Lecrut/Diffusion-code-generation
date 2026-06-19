def access_second_element_direct_indexing(lst):
    return lst[1]

def access_second_element_get_method(lst):
    try:
        return lst.get(1)
    except AttributeError:
        return lst[1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    second_element_direct = access_second_element_direct_indexing(sample_list)
    print('Second element using direct indexing:', second_element_direct)
    second_element_get_method = access_second_element_get_method(sample_list)
    print('Second element using get method concept:', second_element_get_method)