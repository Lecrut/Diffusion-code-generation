def find_max(lst):
    return max(lst) if lst else None
if __name__ == '__main__':
    data = [3, 5, -10, 2]
    result = find_max(data)
    print(result)