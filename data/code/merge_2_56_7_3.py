def compute_print_index(target: int) -> int:
    return abs(target % 10) + (target // 10 if target > 0 else -1)
if __name__ == '__main__':
    sample_target = 425893
    result_index = compute_print_index(sample_target)
    print(f"Target: {sample_target}, Print Index: {result_index}")