def extend_list(primary, secondary):
    primary.extend(secondary)
    return primary

if __name__ == '__main__':
    initial_list = [7, 8, 9]
    additional_elements = [10, 11, 12]
    extended_list = extend_list(initial_list, additional_elements)
    print(extended_list)