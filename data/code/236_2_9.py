sample_pattern = "###\n###\n###"

def repeat_pattern(pattern, n):
    return [pattern] * n

if __name__ == '__main__':
    repeated_output = repeat_pattern(sample_pattern, 10)
    print("--- Repeated Pattern ---")
    for line in repeated_output:
        print(line)