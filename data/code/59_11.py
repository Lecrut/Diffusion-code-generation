def find_middle_optimized(sequence):
    n = len(sequence)
    if n == 0:
        return None
    if n % 2 == 1:
        middle_index = n // 2
        return sequence[middle_index]
    else:
        middle_index_right = n // 2
        middle_index_left = middle_index_right - 1
        return (sequence[middle_index_left] + sequence[middle_index_right]) // 2
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [1, 2, 3, 4]
    list4 = [100]
    list5 = []
    print(f"List 1: {find_middle_optimized(list1)}")
    print(f"List 2: {find_middle_optimized(list2)}")
    print(f"List 3: {find_middle_optimized(list3)}")
    print(f"List 4: {find_middle_optimized(list4)}")
    print(f"List 5: {find_middle_optimized(list5)}")