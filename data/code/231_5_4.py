def create_repeating_block(pattern, num_lines):
    result = []
    block_length = len(pattern)
    for i in range(num_lines):
        line = pattern[i % block_length]
        result.append(line)
    return "\n".join(result)
if __name__ == '__main__':
    pattern_string = "ABC"
    num_lines = 10
    output = create_repeating_block(pattern_string, num_lines)
    print(output)