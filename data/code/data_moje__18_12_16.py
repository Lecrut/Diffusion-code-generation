def calculate_median_index(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        first_half_max = numbers[0]
        for i in range(1, mid):
            if numbers[i] > first_half_max:
                first_half_max = numbers[i]
        second_half_min = numbers[mid]
        for i in range(mid + 1, n):
            if numbers[i] < second_half_min:
                second_half_min = numbers[i]
        return (first_half_max + second_half_min) / 2
    else:
        median_val = numbers[mid]
        for i in range(mid):
            if numbers[i] > median_val:
                median_val = numbers[i]
        for i in range(mid + 1, n):
            if numbers[i] < median_val:
                median_val = numbers[i]
        return median_val

if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5]
    sample_list_even = [10, 20, 30, 40]
    print(calculate_median_index(sample_list_odd))
    print(calculate_median_index(sample_list_even))