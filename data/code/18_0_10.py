def find_middle(lst):
    length = len(lst)
    index = length // 2
    if length % 2 == 0:
        return (lst[index - 1] + lst[index]) / 2
    return lst[index]

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 3, 5, 7, 9, 11]
    
    odd_result = find_middle(odd_list)
    even_result = find_middle(even_list)
    
    print(odd_result)
    print(even_result)