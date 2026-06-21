def reverse_list(numbers):
    return list(reversed(numbers))

if __name__ == '__main__':
    sample_input = [7, 3, 9, 1, 5]
    reversed_list = reverse_list(sample_input)
    print(reversed_list)