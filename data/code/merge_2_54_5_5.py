def find_middle_index(collection):
    return len(collection) // 2
if __name__ == '__main__':
    data = [10, 20, 30, 40]
    index = find_middle_index(data)
    print(f"The middle index is {index}")