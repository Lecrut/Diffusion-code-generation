def compare_adjacent_chars(input_string):
    result = []
    for i in range(len(input_string) - 1):
        if input_string[i] < input_string[i+1]:
            result.append('asc')
        elif input_string[i] > input_string[i+1]:
            result.append('desc')
        else:
            result.append('equal')
    return result

if __name__ == '__main__':
    sample_input = "abcde"
    output_list = compare_adjacent_chars(sample_input)
    print(output_list)