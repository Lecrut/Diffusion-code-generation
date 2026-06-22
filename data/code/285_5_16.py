def compare_adjacent_chars(char_pair):
    return 'asc' if ord(char_pair[0]) < ord(char_pair[1]) else 'desc'

if __name__ == '__main__':
    sample_string = "abcde"
    result_list = [compare_adjacent_chars(sample_string[i:i+2]) for i in range(len(sample_string) - 1)]
    print(result_list)