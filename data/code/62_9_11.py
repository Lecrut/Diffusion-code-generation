def access_second_element_direct_indexing(lst):
    return lst[1]

def access_second_element_get_method(lst):
    if len(lst) > 1:
        return lst[1]
    else:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    second_element_direct_indexing = access_second_element_direct_indexing(sample_list)
    print('Second element using direct indexing:', second_element_direct_indexing)
    second_element_get_method = access_second_element_get_method(sample_list)
    print('Second element using get method-like approach:', second_element_get_method)