def repeat_sequence(input_list, N):
    if N <= 0:
        return []
    return input_list * N
if __name__ == '__main__':
    list1 = [1, 2]
    n1 = 3
    result1 = repeat_sequence(list1, n1)
    print(f"Input: {list1}, N: {n1}")
    print(f"Result: {result1}")
    list2 = ['a', 'b']
    n2 = 2
    result2 = repeat_sequence(list2, n2)
    print(f"Input: {list2}, N: {n2}")
    print(f"Result: {result2}")
    list3 = [10]
    n3 = 5
    result3 = repeat_sequence(list3, n3)
    print(f"Input: {list3}, N: {n3}")
    print(f"Result: {result3}")