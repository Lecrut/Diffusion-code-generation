def sort_and_count(numbers):
    def count_evens(nums):
        return sum(1 for num in nums if num % 2 == 0)
    
    sorted_numbers = sorted(numbers)
    even_count = count_evens(numbers)
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [10, 3, 5, 8, 6, 7, 4, 2]
    result = sort_and_count(sample_values)
    print(result)