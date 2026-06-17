def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    n = len(values)
    if n < 2:
        return values
    try:
        index_a = int(input().strip())
        index_b = int(input().strip())
        if not (0 <= index_a < n and 0 <= index_b < n):
            raise IndexError("Indices out of range.")
        if abs(index_a - index_b) != 1:
            print("Error: Indices must be adjacent.")
            return values
    except ValueError:
        print("Error: Invalid input. Please enter integers.")
        return values
def main():
    data = [5, 3, 8, 2, 9]
    if __name__ == '__main__':
        swap_adjacent(data)
if __name__ == '__main__':
    pass