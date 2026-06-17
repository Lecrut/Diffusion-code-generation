def get_final_value(lst):
    return sum(1 for _ in lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    explicit_count = 0
    for item in sample_list:
        explicit_count += 1
    print(f"Explicit Loop Result: {explicit_count}")
    one_liner_result = sum((lambda x: True)(x) for x in sample_list) or 0
    print(f"One-Liner Result: {one_liner_result}")