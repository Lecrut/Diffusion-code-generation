def run_length_encode(sequence):
    if not sequence:
        return []

    def _encode(index, count, current_element, result):
        if index == len(sequence):
            if current_element is not None:
                result = result + [(current_element, count)]
            return result
        if sequence[index] == current_element:
            return _encode(index + 1, count + 1, current_element, result)
        else:
            if current_element is not None:
                result = result + [(current_element, count)]
            return _encode(index + 1, 1, sequence[index], result)

    return _encode(0, 0, None, [])

if __name__ == '__main__':
    sample = [1, 1, 2, 2, 2, 3, 4, 4]
    encoded = run_length_encode(sample)
    print(encoded)
    sample2 = 'AAABBBCCDAA'
    encoded2 = run_length_encode(sample2)
    print(encoded2)
    sample3 = []
    encoded3 = run_length_encode(sample3)
    print(encoded3)
    sample4 = [5]
    encoded4 = run_length_encode(sample4)
    print(encoded4)