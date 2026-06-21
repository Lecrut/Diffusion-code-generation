def middle_value(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        sorted_numbers = sorted(numbers)
        mid_index = len(sorted_numbers) // 2
        return sorted_numbers[mid_index]

if __name__ == '__main__':
    print(middle_value([3, 1, 4, 1, 5, 9, 2]))
    print(middle_value([]))
    print(middle_value([7]))