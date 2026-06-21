def get_central_item(seq):
    if not seq:
        raise ValueError("Sequence must not be empty")
    n = len(seq)
    index = n // 2
    return seq[index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [100, 200, 300, 400]
    odd_result = get_central_item(odd_list)
    even_result = get_central_item(even_list)
    print(odd_result)
    print(even_result)