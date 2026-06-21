from typing import List, Tuple, Any

def run_length_compress(input_list: List[Any]) -> List[Tuple[Any, int]]:
    if not input_list:
        return []

    compressed = []
    current_char = input_list[0]
    count = 1

    for i in range(1, len(input_list)):
        char = input_list[i]
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    result = run_length_compress(sample_input)
    print(result)