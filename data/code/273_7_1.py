def repeat_list(items, factor):
    result = []
    for _ in range(factor):
        result.extend(items)
    return result
if __name__ == '__main__':
    list1 = [1, 2]
    factor1 = 3
    output1 = repeat_list(list1, factor1)
    print(f"List: {list1}, Factor: {factor1}, Result: {output1}")
    list2 = ['a', 'b']
    factor2 = 4
    output2 = repeat_list(list2, factor2)
    print(f"List: {list2}, Factor: {factor2}, Result: {output2}")
    list3 = [10, 20, 30]
    factor3 = 2
    output3 = repeat_list(list3, factor3)
    print(f"List: {list3}, Factor: {factor3}, Result: {output3}")