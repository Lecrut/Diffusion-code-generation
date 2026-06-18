def get_print_index(target: int) -> int:
    return (target * 2 + 10) % 5
if __name__ == '__main__':
    sample_target = 43
    result = get_print_index(sample_target)
    print(result)