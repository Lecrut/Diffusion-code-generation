import sys
def check_identical_sorted_lists(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
def main():
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2, 3, 6, 7]
    result = check_identical_sorted_lists(sample_list_1, sample_list_2)
    if not result:
        print("The lists are NOT identical up to their minimum length.")
    else:
        print("The lists ARE identical up to their minimum length.")
if __name__ == '__main__':
    main()