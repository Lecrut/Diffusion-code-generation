def count_first_elements(tuple_of_tuples):
    count_dict = {}
    for sub_tuple in tuple_of_tuples:
        if sub_tuple[0] in count_dict:
            count_dict[sub_tuple[0]] += 1
        else:
            count_dict[sub_tuple[0]] = 1
    return count_dict

if __name__ == '__main__':
    sample_data = ((1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'))
    result = count_first_elements(sample_data)
    print(result)