if __name__ == '__main__':
    sample_pattern = ["###", "###", "###"]
    repeat_count = 10
    result = [item for _ in range(repeat_count) for item in sample_pattern]
    print("--- Repeated Pattern ---")
    for line in result:
        print(line)