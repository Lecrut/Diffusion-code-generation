def are_sums_different(list1, list2):
    if not isinstance(list1, (list, tuple)) or not isinstance(list2, (list, tuple)):
        raise ValueError("Both inputs must be lists or tuples.")
    
    def calculate_sum(numbers):
        total = 0
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("All elements in the list must be numbers.")
            total += num
        return total
    
    sum1 = calculate_sum(list1)
    sum2 = calculate_sum(list2)
    
    return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 4, 3, 2, 0]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)