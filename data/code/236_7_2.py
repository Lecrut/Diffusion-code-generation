import sys
def generate_pattern(line):
    pattern = ""
    for _ in range(10):
        pattern += line + "\n"
    return pattern
if __name__ == '__main__':
    single_line = "X"
    result = generate_pattern(single_line)
    print(result)