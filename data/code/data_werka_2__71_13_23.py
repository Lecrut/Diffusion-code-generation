MIDDLE_OFFSET_EVEN = 1
MIDDLE_OFFSET_ODD = 0

def get_middle_element(data):
    if not data:
        raise ValueError("List must not be empty")
    length = len(data)
    index = length // 2
    if length % 2 == 0:
        index -= MIDDLE_OFFSET_EVEN
    return data[index]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([10, 20, 30, 40]))
    print(get_middle_element([100]))
    print(get_middle_element([1, 2]))
    print(get_middle_element([5, 10, 15, 20, 25, 30]))