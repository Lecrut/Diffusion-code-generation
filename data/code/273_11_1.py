def repeat_sequence(sequence):
    result = []
    for _ in range(3):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    input_list = ["a", "b"]
    output_list = repeat_sequence(input_list)
    print(output_list)