def find_matching_pair_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                yield True
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    result_generator = find_matching_pair_generator(list_a, list_b)
    found_matches = []
    for match in result_generator:
        found_matches.append(match)
    print(found_matches)