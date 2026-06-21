def retrieve_elements(numbers):
    if not numbers:
        return ()
    first = numbers[0]
    last = numbers[-1]
    middle_index = len(numbers) // 2
    middle = numbers[middle_index]
    return (first, last, middle)

if __name__ == '__main__':
    example_list = [3, 6, 9, 12, 15, 18, 21]
    elements = retrieve_elements(example_list)
    print(elements)