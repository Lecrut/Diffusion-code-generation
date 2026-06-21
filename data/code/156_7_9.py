def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [10, 20, 30]
    empty_list = []
    
    print(f"Average of {sample_list_1}: {calculate_average(sample_list_1)}")
    print(f"Average of {sample_list_2}: {calculate_average(sample_list_2)}")
    print(f"Average of {empty_list}: {calculate_average(empty_list)}")