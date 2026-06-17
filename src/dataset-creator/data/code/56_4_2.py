def get_print_index(target: int) -> int:
    return hash(str(target)) % 10
if __name__ == '__main__':
    sample_target = 42
    result = get_print_index(sample_target)
    print(result)