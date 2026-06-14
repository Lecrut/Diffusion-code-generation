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
    sample_strings = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    result1 = arrange_in_square_grid(sample_strings)
    print("--- Sample 1 ---")
    for row in result1:
        print(row)
    sample_strings_2 = ["A", "B", "C", "D", "E", "F", "G"]
    result2 = arrange_in_square_grid(sample_strings_2)
    print("\n--- Sample 2 ---")
    for row in result2:
        print(row)
    sample_strings_3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    result3 = arrange_in_square_grid(sample_strings_3)
    print("\n--- Sample 3 ---")
    for row in result3:
        print(row)
    sample_strings_4 = ["a", "b", "c", "d", "e", "f", "g"]
    result4 = arrange_in_square_grid(sample_strings_4)
    print("\n--- Sample 4 ---")
    for row in result4:
        print(row)