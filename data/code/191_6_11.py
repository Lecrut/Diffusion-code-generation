LIST_A = ["apple", "banana"]
LIST_B = ["cherry", "date"]

def combine_lists(list_alpha, list_beta):
    combined_list = list_alpha.copy()
    combined_list.extend(list_beta)
    return combined_list

if __name__ == '__main__':
    result = combine_lists(LIST_A, LIST_B)
    print(result)