def sort_integers(data):
    if not all(isinstance(i, int) for i in data):
        raise ValueError("All elements in the list must be integers.")
    return sorted(data)

if __name__ == '__main__':
    numbers = [5, 2, 8, 1, 9, 3]
    try:
        result = sort_integers(numbers)
        print(result)
    except ValueError as e:
        print(e)