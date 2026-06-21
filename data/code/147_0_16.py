def sort_ascending(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    return sorted(numbers)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    try:
        sorted_list = sort_ascending(sample_list)
        print(sorted_list)
    except ValueError as e:
        print(e)