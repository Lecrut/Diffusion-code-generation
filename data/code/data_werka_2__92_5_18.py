BOOLEAN_TRUE = True
BOOLEAN_FALSE = False
NEGATION_MAP = {BOOLEAN_TRUE: BOOLEAN_FALSE, BOOLEAN_FALSE: BOOLEAN_TRUE}

def generate_opposite_truth_values(input_stream):
    for item in input_stream:
        if item in NEGATION_MAP:
            yield NEGATION_MAP[item]
        else:
            raise ValueError(f"Expected boolean, got {type(item)}")

if __name__ == '__main__':
    test_data = [True, False, False, True, True, False]
    output_stream = generate_opposite_truth_values(test_data)
    result_list = list(output_stream)
    print(result_list)