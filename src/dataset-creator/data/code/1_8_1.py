import sys
def check_identical_sorted(list_a: list[int], list_b: list[int]) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2, 3, 6, 7]
    result = check_identical_sorted(sample_list_1, sample_list_2)
    print(f"Are the lists identical up to minimum length? {result}")