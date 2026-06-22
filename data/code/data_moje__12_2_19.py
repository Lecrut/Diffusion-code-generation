def get_central_item(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[(length // 2) - 1]

if __name__ == '__main__':
    odd_sequence = [10, 20, 30, 40, 50]
    even_sequence = [10, 20, 30, 40]
    single_item = [42]
    string_sequence = "Python"
    
    print(get_central_item(odd_sequence))
    print(get_central_item(even_sequence))
    print(get_central_item(single_item))
    print(get_central_item(string_sequence))