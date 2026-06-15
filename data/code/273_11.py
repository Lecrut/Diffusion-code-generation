def repeat_sequence(sequence):
    repeated_list = []
    for _ in range(3):
        repeated_list.extend(sequence)
    return repeated_list
if __name__ == '__main__':
    input_list = ["a", "b"]
    result = repeat_sequence(input_list)
    print(result)