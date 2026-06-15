def rotate_list(names, rotations):
    n = len(names)
    if n == 0:
        return []
    rotations = rotations % n
    if rotations == 0:
        return list(names)
    else:
        rotated_list = names[n - rotations:] + names[:n - rotations]
        return rotated_list
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    rotation_amount = 2
    result = rotate_list(sample_names, rotation_amount)
    print(result)