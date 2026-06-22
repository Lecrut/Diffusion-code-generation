def repeat_pattern(pattern, n):
    return [item for _ in range(n) for item in pattern]

if __name__ == '__main__':
    sample_pattern = ["###", "###", "###"]
    repeat_count = 10
    repeated_output = repeat_pattern(sample_pattern, repeat_count)
    print("--- Repeated Pattern ---")
    print(repeated_output)