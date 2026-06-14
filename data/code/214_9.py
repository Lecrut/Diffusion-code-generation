import sys
def find_smallest_string(string_list):
    if not string_list:
        return None
    smallest = string_list[0]
    for s in string_list[1:]:
        if s < smallest:
            smallest = s
    return smallest
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat", "apricot"]
    result = find_smallest_string(sample_list)
    print(result)