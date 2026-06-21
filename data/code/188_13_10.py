def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(original_list)
    print(f"Original: {original_list}")
    print(f"Reversed: {reversed_list}")

    another_list = ['apple', 'banana', 'cherry']
    reversed_another_list = reverse_list(another_list)
    print(f"Original: {another_list}")
    print(f"Reversed: {reversed_another_list}")