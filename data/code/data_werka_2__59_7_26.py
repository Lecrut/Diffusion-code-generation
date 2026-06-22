def find_middle_item(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [100, 200, 300, 400, 500]
    sample_list_even = [50, 100, 150, 200, 250, 300]
    middle_odd = find_middle_item(sample_list_odd)
    middle_even = find_middle_item(sample_list_even)
    print("Middle item of odd list:", middle_odd)
    print("Middle item of even list:", middle_even)