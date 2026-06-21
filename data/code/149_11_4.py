def reverse_list_in_place(strings):
    strings.reverse()

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print("Original list:", sample_strings)
    reverse_list_in_place(sample_strings)
    print("Reversed list:", sample_strings)