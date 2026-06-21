def remove_duplicates(data, exclude_item):
    seen = set()
    for item in data:
        if item != exclude_item and item not in seen:
            seen.add(item)
            yield item

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 2, 3]
    exclude = 3
    filtered_generator = remove_duplicates(input_list, exclude)
    result_list = list(filtered_generator)
    print(result_list)