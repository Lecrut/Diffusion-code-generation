def repeat_sequence(sequence):
    repeated = []
    for _ in range(3):
        repeated.extend(sequence)
    return repeated
if __name__ == '__main__':
    input_list = ["a", "b"]
    result = repeat_sequence(input_list)
    print(result)