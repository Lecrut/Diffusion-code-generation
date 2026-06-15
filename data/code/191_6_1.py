def combine_lists(list_alpha, list_beta):
    combined = []
    for item in list_alpha:
        combined.append(item)
    for item in list_beta:
        combined.append(item)
    return combined
if __name__ == '__main__':
    list_a = ["apple", "banana"]
    list_b = ["cherry", "date"]
    result = combine_lists(list_a, list_b)
    print(result)