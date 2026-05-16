def combine_lists(list_alpha, list_beta):
    result = []
    i = 0
    j = 0
    n = len(list_alpha)
    m = len(list_beta)
    while i < n and j < m:
        if list_alpha[i] < list_beta[j]:
            result.append(list_alpha[i])
            i += 1
        else:
            result.append(list_beta[j])
            j += 1
    result.extend(list_alpha[i:])
    result.extend(list_beta[j:])
    return result
if __name__ == '__main__':
    list_alpha = [1, 5, 8, 10]
    list_beta = [2, 3, 6, 9, 11]
    combined = combine_lists(list_alpha, list_beta)
    print(combined)