PATTERN = "###\n###\n###"
REPEAT_COUNT = 10

def repeat_pattern(pattern, n):
    return [item for sublist in [[pattern] * n] for item in sublist]

if __name__ == '__main__':
    repeated_output = repeat_pattern(PATTERN, REPEAT_COUNT)
    print("--- Repeated Pattern ---")
    for line in repeated_output:
        print(line)