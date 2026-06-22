def find_middle_element(t):
    if not t:
        raise ValueError("Tuple is empty")
    return t[len(t) // 2]

if __name__ == '__main__':
    print(find_middle_element((1, 2, 3)))
    print(find_middle_element((1, 2, 3, 4, 5)))
    print(find_middle_element((42,)))
    try:
        print(find_middle_element(()))
    except ValueError as e:
        print(e)