def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    SAMPLE_VALUES = [7, 2, 5, 3, 8, 6]
    DESCENDING_ORDERED = sort_by_descending(SAMPLE_VALUES)
    print(DESCENDING_ORDERED)