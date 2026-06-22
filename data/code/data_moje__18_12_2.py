def median_index_value(lst):
    n = len(lst)
    if n == 0:
        raise ValueError('List must not be empty')
    original_indices = list(range(n))
    working_indices = list(original_indices)
    working_values = list(lst)
    target_k = n // 2
    left = 0
    right = n - 1
    while left <= right:
        pivot_index = left
        pivot_value = working_values[pivot_index]
        lt = left
        gt = right
        i = left
        while i <= gt:
            if working_values[i] < pivot_value:
                working_values[i], working_values[lt] = (working_values[lt], working_values[i])
                working_indices[i], working_indices[lt] = (working_indices[lt], working_indices[i])
                lt += 1
                i += 1
            elif working_values[i] > pivot_value:
                working_values[i], working_values[gt] = (working_values[gt], working_values[i])
                working_indices[i], working_indices[gt] = (working_indices[gt], working_indices[i])
                gt -= 1
            else:
                i += 1
        if lt - 1 == target_k:
            return working_indices[target_k]
        elif target_k < lt:
            right = lt - 1
        else:
            left = gt + 1
    return working_indices[target_k]
if __name__ == '__main__':
    sample_list = [10, 5, 8, 3, 2]
    result = median_index_value(sample_list)
    print(result)