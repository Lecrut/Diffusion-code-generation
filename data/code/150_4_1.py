def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 1, 9, 2, 3]
    unique_list = remove_duplicates(sample_list)
    print(unique_list)