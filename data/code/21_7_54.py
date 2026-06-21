DESCENDING_ORDER = True

def sort_by_descending(numbers):
    return sorted(numbers, reverse=DESCENDING_ORDER)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 4, 6]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)