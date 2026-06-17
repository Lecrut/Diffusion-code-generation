def get_final_value(lst):
    return sum(1 for _ in lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    one_liner_result = len(sample_list)
    explicit_loop_count = 0
    for item in sample_list:
        explicit_loop_count += 1
    print(f"One-liner result: {one_liner_result}, Loop count: {explicit_loop_count}")