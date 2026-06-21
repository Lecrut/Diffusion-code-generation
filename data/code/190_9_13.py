import bisect

def contains_integer(sorted_numbers, target):
    index = bisect.bisect_left(sorted_numbers, target)
    return index != len(sorted_numbers) and sorted_numbers[index] == target

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(f"Contains 5: {contains_integer(sample_list, 5)}")
    print(f"Contains 2: {contains_integer(sample_list, 2)}")