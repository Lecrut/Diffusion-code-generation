PATTERN = "###\n###\n###"
REPEAT_COUNT = 10

def repeat_pattern(pattern, n):
    return [item for _ in range(n) for item in pattern.split('\n')]

if __name__ == '__main__':
    repeated_list = repeat_pattern(PATTERN, REPEAT_COUNT)
    print("--- Repeated Pattern ---")
    print("\n".join(repeated_list))