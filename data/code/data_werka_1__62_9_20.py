def access_second_item_direct_indexing(lst):
    return lst[1]

def access_second_item_get_method(lst):
    return lst.get(1) if hasattr(lst, 'get') else None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    second_item_direct_indexing = access_second_item_direct_indexing(sample_list)
    print('Second item using direct indexing:', second_item_direct_indexing)
    second_item_get_method = access_second_item_get_method(sample_list)
    print('Second item using .get() method (conceptual):', second_item_get_method)