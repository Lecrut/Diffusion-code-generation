def run_length_encode(sequence):
    if not sequence:
        return []

    result = []
    current_item = sequence[0]
    count = 1

    for item in sequence[1:]:
        if item is current_item:
            count += 1
        else:
            result.append((count, current_item))
            current_item = item
            count = 1

    result.append((count, current_item))
    return result

if __name__ == '__main__':
    data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    encoded = run_length_encode(data)
    print(encoded)

    data2 = ['a', 'a', 'b', 'b', 'b', 'c']
    encoded2 = run_length_encode(data2)
    print(encoded2)

    data3 = []
    encoded3 = run_length_encode(data3)
    print(encoded3)

    data4 = [None, None, None, 0, 0]
    encoded4 = run_length_encode(data4)
    print(encoded4)