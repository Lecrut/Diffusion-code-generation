def sort_integers(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements in the list must be integers.")
    return sorted(data)

if __name__ == '__main__':
    numbers = [5, 2, 8, 1, 9, 3]
    try:
        sorted_numbers = sort_integers(numbers)
        print(sorted_numbers)
    except ValueError as e:
        print(e)