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
    sample_numbers = [34, 7, 23, 32, 56, 19, 8]
    even_list, odd_list = partition_and_sort(sample_numbers)
    print("Even List:", even_list)
    print("Odd List:", odd_list)