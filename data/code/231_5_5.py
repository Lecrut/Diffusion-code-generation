def create_repeating_block(block, num_lines):
    result = ""
    for _ in range(num_lines):
        result += block + "\n"
    return result
if __name__ == '__main__':
    block_string = "Hello World"
    num_lines = 5
    output = create_repeating_block(block_string, num_lines)
    print(output)