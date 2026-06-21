MAX_NUMBER = float('-inf')

def flatten_and_find_largest(nested_list):
    flattened_list = []
    
    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                flatten(item)
            else:
                flattened_list.append(item)
                
    flatten(nested_list)
    largest = MAX_NUMBER
    for number in flattened_list:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [12, 45, [67, [89, 34], 91], 5]
    result = flatten_and_find_largest(sample_list)
    print(result)