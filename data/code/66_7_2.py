def compare_adjacent_numbers(data):
    for i in range(len(data) - 1):
        if not isinstance(data[i], (int, float)) or not isinstance(data[i+1], (int, float)):
            raise TypeError("Adjacent elements must both be numerical.")
        num1 = data[i]
        num2 = data[i+1]
        if num1 != num2:
            return f"Difference found between {num1} and {num2}"
    return "All adjacent elements are equal"
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 'a', 4, 5]
    list3 = [1.5, 2.5, 3.5]
    list4 = [1, '2', 3]
    list5 = [1, 2, 3, 4, 5, 6]
    print(f"List 1: {list1}")
    try:
        result1 = compare_adjacent_numbers(list1)
        print(f"Result 1: {result1}")
    except TypeError as e:
        print(f"Error 1: {e}")
    print("-" * 20)
    print(f"List 2: {list2}")
    try:
        result2 = compare_adjacent_numbers(list2)
        print(f"Result 2: {result2}")
    except TypeError as e:
        print(f"Error 2: {e}")
    print("-" * 20)
    print(f"List 3: {list3}")
    try:
        result3 = compare_adjacent_numbers(list3)
        print(f"Result 3: {result3}")
    except TypeError as e:
        print(f"Error 3: {e}")
    print("-" * 20)
    print(f"List 4: {list4}")
    try:
        result4 = compare_adjacent_numbers(list4)
        print(f"Result 4: {result4}")
    except TypeError as e:
        print(f"Error 4: {e}")
    print("-" * 20)
    print(f"List 5: {list5}")
    try:
        result5 = compare_adjacent_numbers(list5)
        print(f"Result 5: {result5}")
    except TypeError as e:
        print(f"Error 5: {e}")