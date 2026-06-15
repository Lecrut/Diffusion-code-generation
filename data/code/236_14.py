import sys
def print_pattern(rows, pattern):
    output = []
    for _ in range(5):
        line = ""
        for i in range(rows):
            if i < len(pattern):
                line += pattern[i] + " "
            else:
                line += "  "
        output.append(line.rstrip())
    print('\n'.join(output))
if __name__ == '__main__':
    num_rows = 10
    pattern_string = '#'
    print_pattern(num_rows, pattern_string)