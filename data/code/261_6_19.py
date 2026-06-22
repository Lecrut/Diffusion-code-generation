def calculate_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    sorted_data = sorted(data)
    n = len(sorted_data)

    def get_middle_index(n):
        return n // 2
    middle_index = get_middle_index(n)
    if n % 2 == 1:
        return sorted_data[middle_index]
    else:
        mid1 = sorted_data[middle_index - 1]
        mid2 = sorted_data[middle_index]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    print(calculate_median([3, 1, 2, 4, 5]))
    print(calculate_median([-10, 4, 6, 1000, 10, 20]))