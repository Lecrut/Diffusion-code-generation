def combine_lists(list_alpha, list_beta):
    combined = list_alpha.copy()
    combined.extend(list_beta)
    return combined

if __name__ == '__main__':
    LIST_A = ["apple", "banana"]
    LIST_B = ["cherry", "date"]
    result = combine_lists(LIST_A, LIST_B)
    print(result)