def reverse_list(numbers):
    return list(reversed(numbers))

if __name__ == '__main__':
    sample_input = [8, 3, 5, 7, 1]
    reversed_list = reverse_list(sample_input)
    print(reversed_list)