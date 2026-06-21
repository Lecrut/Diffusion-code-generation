def merge_set_lists(list_alpha, list_beta):
    combined_sets = set().union(*list_alpha)
    combined_sets.update(set().union(*list_beta))
    return combined_sets

if __name__ == '__main__':
    list_alpha = [{1, 2}, {3, 4}]
    list_beta = [{5, 6}, {7, 8}]
    result = merge_set_lists(list_alpha, list_beta)
    print(result)