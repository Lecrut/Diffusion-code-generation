def find_matching_tuples(dict1, dict2):
    for key, value1 in dict1.items():
        if key in dict2:
            value2 = dict2[key]
            yield (key, value1, value2)
if __name__ == '__main__':
    large_dict1 = {f'a{i}': i for i in range(100000)}
    large_dict2 = {f'a{i}': i * 2 for i in range(100000)}
    matching_generator = find_matching_tuples(large_dict1, large_dict2)
    results = list(matching_generator)
    print(f"Found {len(results)} matching tuples.")
    if results:
        print("First 5 results:")
        for item in results[:5]:
            print(item)