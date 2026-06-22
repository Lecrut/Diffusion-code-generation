def sort_and_count(numbers):
    even_count = 0
    sorted_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        sorted_numbers.append(num)
    
    sorted_numbers.sort()
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [4, 1, 3, 2, 8, 5, 7, 6]
    result = sort_and_count(sample_values)
    print(result)