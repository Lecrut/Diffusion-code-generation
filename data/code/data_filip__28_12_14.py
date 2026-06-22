def run_length_encode(char_list):
    if not char_list:
        return []

    result = []
    current_char = char_list[0]
    count = 1

    for char in char_list[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']
    print(run_length_encode(sample))