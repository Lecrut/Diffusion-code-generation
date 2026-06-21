MIDDLE_INDEX = lambda n: n // 2

def find_middle(data):
    if not data:
        return None
    n = len(data)
    middle_index = MIDDLE_INDEX(n)
    if n % 2 == 1:
        return data[middle_index]
    else:
        return data[MIDDLE_INDEX(n - 1)]
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(find_middle(sample_data))