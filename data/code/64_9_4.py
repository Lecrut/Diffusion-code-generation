def find_final_index(data: list, target) -> int:
    try:
        last_index = data.index(target)
        while last_index + 1 < len(data) and data[last_index + 1] == target:
            last_index += 1
        return last_index
    except ValueError:
        raise ValueError(f"{target} not found in the list.")
if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 2, 2, 4]
    target1 = 2
    print(f"List: {list1}, Target: {target1}, Final Index: {find_final_index(list1, target1)}")
    list2 = ['a', 'b', 'c', 'b', 'b', 'd']
    target2 = 'b'
    print(f"List: {list2}, Target: {target2}, Final Index: {find_final_index(list2, target2)}")
    list3 = [10, 20, 30]
    target3 = 10
    print(f"List: {list3}, Target: {target3}, Final Index: {find_final_index(list3, target3)}")
    list4 = [5, 5, 5, 5]
    target4 = 5
    print(f"List: {list4}, Target: {target4}, Final Index: {find_final_index(list4, target4)}")
    try:
        list5 = [1, 2, 3]
        target5 = 99
        find_final_index(list5, target5)
    except ValueError as e:
        print(f"Error caught: {e}")