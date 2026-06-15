import math
def arrange_in_square_grid(strings):
    if not strings:
        return []
    n = len(strings)
    side_length = math.ceil(math.sqrt(n))
    grid = []
    for i in range(side_length):
        row = []
        for j in range(side_length):
            index = i * side_length + j
            if index < n:
                row.append(strings[index])
            else:
                row.append("") 
        grid.append(row)
    return grid
if __name__ == '__main__':
    sample_list1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    print("Sample 1:")
    result1 = arrange_in_square_grid(sample_list1)
    for row in result1:
        print(row)
    sample_list2 = ["a", "b", "c", "d", "e", "f", "g"]
    print("\nSample 2:")
    result2 = arrange_in_square_grid(sample_list2)
    for row in result2:
        print(row)
    sample_list3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    print("\nSample 3:")
    result3 = arrange_in_square_grid(sample_list3)
    for row in result3:
        print(row)
    sample_list4 = ["a", "b", "c", "d", "e", "f"]
    print("\nSample 4:")
    result4 = arrange_in_square_grid(sample_list4)
    for row in result4:
        print(row)