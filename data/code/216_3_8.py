def middle_value(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        sorted_numbers = sorted(numbers)
        index = len(sorted_numbers) // 2
        return sorted_numbers[index]

if __name__ == '__main__':
    print(middle_value([3, 1, 4, 1, 5, 9]))
    print(middle_value([7]))
    print(middle_value([]))