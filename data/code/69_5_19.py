def print_list_with_index(lst):
    for i in range(len(lst)):
        print(f"Index: {i}, Value: {lst[i]}")

if __name__ == '__main__':
    mixed_list = [1, "hello", 3.14, True]
    print_list_with_index(mixed_list)