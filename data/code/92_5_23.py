def toggle_boolean_values(stream):
    def apply_logic(x):
        return not x
    return (apply_logic(item) for item in stream)

if __name__ == '__main__':
    input_sequence = [False, True, True, False, False, True]
    generator_output = toggle_boolean_values(input_sequence)
    result_list = list(generator_output)
    print(result_list)