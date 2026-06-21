MIDDLE_OFFSET = 0

def extract_middle(array):
    if not array:
        return None
    index = len(array) // 2
    return array[index + MIDDLE_OFFSET]

if __name__ == '__main__':
    odd_array = [1, 2, 3, 4, 5]
    even_array = [1, 2, 3, 4, 5, 6]
    single_array = [99]
    
    print(extract_middle(odd_array))
    print(extract_middle(even_array))
    print(extract_middle(single_array))
    print(extract_middle([]))