def find_min(values):
    if not values:
        raise ValueError("List is empty")
    min_val = values[0]
    for num in values:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 67, 22, 5, 99, 1, 54]
    print(find_min(sample_list))