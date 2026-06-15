import sys
def generate_pattern(line_content, repetitions):
    full_pattern = ""
    for _ in range(repetitions):
        full_pattern += line_content + "\n"
    return full_pattern
if __name__ == '__main__':
    line = "X"
    repetitions = 10
    result = generate_pattern(line, repetitions)
    print(result)