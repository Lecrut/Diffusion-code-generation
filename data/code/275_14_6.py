def count_first_elements(tuple_of_tuples):
    result = {}
    for item in tuple_of_tuples:
        if item[0] in result:
            result[item[0]] += 1
        else:
            result[item[0]] = 1
    return result

if __name__ == '__main__':
    sample_data = ((1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'))
    print(count_first_elements(sample_data))