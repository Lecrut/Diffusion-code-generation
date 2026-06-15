import sys
def print_pattern_repeated(rows, pattern, repetitions):
    line = ""
    for _ in range(repetitions):
        line += pattern * rows + "\n"
    print(line, end="")
if __name__ == '__main__':
    rows = 5
    pattern = '#'
    repetitions = 5
    print_pattern_repeated(rows, pattern, repetitions)