def sort_and_count(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    sorted_numbers = sorted(numbers)
    return (sorted_numbers, even_count)
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 10, 3, 6]
    sorted_list, count = sort_and_count(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Sorted list: {sorted_list}")
    print(f"Count of even numbers: {count}")