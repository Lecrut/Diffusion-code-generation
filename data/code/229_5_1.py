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
    sample_strings1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    result1 = arrange_in_square_grid(sample_strings1)
    print("Sample 1:")
    for row in result1:
        print(row)
    sample_strings2 = ["a", "b", "c", "d", "e", "f", "g"]
    result2 = arrange_in_square_grid(sample_strings2)
    print("\nSample 2:")
    for row in result2:
        print(row)
    sample_strings3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    result3 = arrange_in_square_grid(sample_strings3)
    print("\nSample 3:")
    for row in result3:
        print(row)
    sample_strings4 = ["a", "b", "c", "d", "e"]
    result4 = arrange_in_square_grid(sample_strings4)
    print("\nSample 4:")
    for row in result4:
        print(row)