def find_first_duplicate(lst):
    encountered = set()
    for element in lst:
        if element in encountered:
            return element
        encountered.add(element)
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 20]
    print(find_first_duplicate(sample_list))