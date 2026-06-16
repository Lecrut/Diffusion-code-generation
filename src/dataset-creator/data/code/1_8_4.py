import sys
def check_identical_up_to_min_length(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
def main():
    sample_list_1 = [3, 5, 7, 9, 11]
    sample_list_2 = [3, 5, 8, 9, 10]
    result = check_identical_up_to_min_length(sample_list_1, sample_list_2)
    if result:
        print("Lists are identical up to their minimum length.")
    else:
        print("Lists differ before reaching the end of either list.")
if __name__ == '__main__':
    main()