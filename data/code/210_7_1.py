def calculate_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum
if __name__ == '__main__':
    list1 = [10, 5.5, 20, 3.14]
    result1 = calculate_range(list1)
    print(f"List: {list1}, Range: {result1}")
    list2 = [-5, 100, 0.5, -10]
    result2 = calculate_range(list2)
    print(f"List: {list2}, Range: {result2}")
    list3 = [7, 7, 7]
    result3 = calculate_range(list3)
    print(f"List: {list3}, Range: {result3}")
    list4 = []
    result4 = calculate_range(list4)
    print(f"List: {list4}, Range: {result4}")