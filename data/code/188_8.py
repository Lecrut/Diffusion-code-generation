def reverse_list_recursive(data):
    if not data:
        return []
    else:
        return [data[-1]] + reverse_list_recursive(data[:-1])
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_recursive(sample_list)
    print(reversed_list)