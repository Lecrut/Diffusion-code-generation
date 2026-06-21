def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    
    avg_sample = calculate_average(sample_list)
    print(f"The average of {sample_list} is: {avg_sample}")
    
    avg_empty = calculate_average(empty_list)
    print(f"The average of an empty list is: {avg_empty}")