def find_middle(data):
    if not data:
        raise ValueError("List must not be empty")
    length = len(data)
    mid = length // 2
    if length % 2 == 1:
        return data[mid]
    return (data[mid - 1] + data[mid]) / 2.0

if __name__ == '__main__':
    odd_sample = [10, 20, 30, 40, 50]
    even_sample = [10, 20, 30, 40]
    print(find_middle(odd_sample))
    print(find_middle(even_sample))