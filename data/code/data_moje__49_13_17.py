STAR_DIMENSION = 6

def construct_star_square(side_length):
    single_row = '*' * side_length
    row_collection = []
    counter = 0
    while counter < side_length:
        row_collection.append(single_row)
        counter += 1
    output_string = '\n'.join(row_collection)
    return output_string

if __name__ == '__main__':
    dimension_value = 6
    result = construct_star_square(dimension_value)
    print(result)