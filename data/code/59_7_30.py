def find_middle_item(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    odd_length_list = [5, 10, 15, 20, 25]
    even_length_list = [1, 2, 3, 4, 5, 6]
    
    middle_odd = find_middle_item(odd_length_list)
    middle_even = find_middle_item(even_length_list)
    
    print(f"Middle item of odd length list: {middle_odd}")
    print(f"Middle item of even length list: {middle_even}")