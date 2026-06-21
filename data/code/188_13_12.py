def reverse_list(iterable):
    if not isinstance(iterable, list):
        raise ValueError("Input must be a list")
    return iterable[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    print(f"Original: {sample}, Reversed: {reverse_list(sample)}")