def get_print_index(target: int) -> int:
    return target % 10
if __name__ == '__main__':
    sample_targets = [5, 27, 99]
    results = {target: get_print_index(target) for target in sample_targets}
    output_lines = []
    print("Target\tIndex")
    for target, index in sorted(results.items()):
        output_lines.append(f"{target}\t{index}")