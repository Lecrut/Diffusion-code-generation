def reverse_string_recursive(s):
    def helper(index):
        if index == 0:
            return s[0]
        else:
            return helper(index - 1) + s[index]
    return helper(len(s) - 1)

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_string = "example"
    reversed_by_recursion = reverse_string_recursive(sample_string)
    reversed_by_slicing = reverse_string_slicing(sample_string)
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)