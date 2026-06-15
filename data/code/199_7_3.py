def rotate_list(names, rotations):
    n = len(names)
    if n == 0:
        return []
    rotations = rotations % n
    rotated_list = names[-rotations:] + names[:-rotations]
    return rotated_list
if __name__ == '__main__':
    names1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
    rotations1 = 2
    result1 = rotate_list(names1, rotations1)
    print(f"Original: {names1}")
    print(f"Rotations: {rotations1}")
    print(f"Result: {result1}")
    names2 = ["A", "B", "C", "D"]
    rotations2 = 6
    result2 = rotate_list(names2, rotations2)
    print(f"Original: {names2}")
    print(f"Rotations: {rotations2}")
    print(f"Result: {result2}")
    names3 = ["One", "Two", "Three"]
    rotations3 = -1
    result3 = rotate_list(names3, rotations3)
    print(f"Original: {names3}")
    print(f"Rotations: {rotations3}")
    print(f"Result: {result3}")
    names4 = ["X", "Y"]
    rotations4 = 5
    result4 = rotate_list(names4, rotations4)
    print(f"Original: {names4}")
    print(f"Rotations: {rotations4}")
    print(f"Result: {result4}")