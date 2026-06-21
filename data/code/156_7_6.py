def compute_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list1 = [5, 7, 9]
    sample_list2 = [-2, 0, 2]
    empty_list = []
    
    avg1 = compute_average(sample_list1)
    print(f"The average of {sample_list1} is: {avg1}")
    
    avg2 = compute_average(sample_list2)
    print(f"The average of {sample_list2} is: {avg2}")
    
    avg3 = compute_average(empty_list)
    if avg3 is None:
        print("The list is empty, no average to calculate.")