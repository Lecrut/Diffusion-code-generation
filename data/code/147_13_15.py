def sort_floats(lst):
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only floating-point numbers.")
    return sorted(lst)

if __name__ == '__main__':
    print(sort_floats([3.5, 1.2, 4.8, 2.1]))