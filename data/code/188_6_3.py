def reverse_generator(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, (int, str)) for item in lst):
        raise ValueError("List items must be integers or strings")
    
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

if __name__ == '__main__':
    sample_list = [10, "world", 30]
    for item in reverse_generator(sample_list):
        print(item)