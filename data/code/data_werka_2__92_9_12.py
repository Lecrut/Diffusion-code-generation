BOOL_INVERSION = [False, True]

def find_opposite_truth(value):
    if value:
        current_index = 1
    else:
        current_index = 0
    return BOOL_INVERSION[current_index]

if __name__ == '__main__':
    sample_input_a = False
    sample_input_b = True
    output_a = find_opposite_truth(sample_input_a)
    output_b = find_opposite_truth(sample_input_b)
    print(output_a)
    print(output_b)