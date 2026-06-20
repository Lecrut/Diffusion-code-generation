def partition_and_sort(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    even.sort()
    odd.sort()

    return even, odd

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even_list, odd_list = partition_and_sort(sample_numbers)
    print("Even:", even_list)
    print("Odd:", odd_list)