def list_concatenator(list_one, list_two):
    return list_one + list_two

if __name__ == '__main__':
    first_sequence = [1, 2, 3]
    second_sequence = [4, 5, 6]
    concatenated_result = list_concatenator(first_sequence, second_sequence)
    print(concatenated_result)