def is_pair_ascending_or_descending(char1, char2):
    return ord(char2) - ord(char1)

def analyze_adjacent_pairs(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    results = []
    for i in range(len(input_string) - 1):
        result = is_pair_ascending_or_descending(input_string[i], input_string[i + 1])
        if result > 0:
            results.append('A')
        elif result < 0:
            results.append('D')
        else:
            results.append('=')
    return results

if __name__ == '__main__':
    sample_string = "abcde"
    print(analyze_adjacent_pairs(sample_string))