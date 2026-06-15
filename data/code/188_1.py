def reverse_list(input_list):
    return input_list[::-1]
if __name__ == '__main__':
    original = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(original)
    print(reversed_list)
    print(original)