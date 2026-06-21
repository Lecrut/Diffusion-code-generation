def reverse_using_iter(lst):
    return list(reversed(lst))

if __name__ == '__main__':
    input_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = reverse_using_iter(input_data)
    print(result)