def create_repeating_pattern(pattern, num_lines):
    result = ""
    for _ in range(num_lines):
        result += pattern + "\n"
    return result.rstrip('\n')
if __name__ == '__main__':
    pattern_string = "Hello World"
    number_of_lines = 5
    output = create_repeating_pattern(pattern_string, number_of_lines)
    print(output)