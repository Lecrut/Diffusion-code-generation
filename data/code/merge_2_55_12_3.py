def swap_neighbors(lst):
    return [lst[i+1] if i % 2 else lst[i-1] for i in range(len(lst)-1)] + [lst[-1]] if len(lst) > 0 else []
if __name__ == '__main__':
    data = [5, 3, 8, 2, 9, 4]
    result = swap_neighbors(data)
    print(result)