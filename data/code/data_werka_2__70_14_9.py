def get_boundary_items(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    return sequence[0], sequence[-1]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(get_boundary_items(data))