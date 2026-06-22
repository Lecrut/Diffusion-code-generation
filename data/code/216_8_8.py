def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    print(find_middle([1, 2, 3, 4, 5]))
    print(find_middle([10, 20, 30]))
    print(find_middle([7]))