def get_final_value(lst):
    return sum(1 for _ in lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    explicit_count = 0
    for _ in sample_list:
        explicit_count += 1
    print(f"Explicit Loop Result: {explicit_count}")
    one_liner_result = sum(1 for item in sample_list if isinstance(item, int))
    print(f"One-Liner Result: {one_liner_result}")