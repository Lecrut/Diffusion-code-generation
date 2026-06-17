def count_elements(iterable):
    count = 0
    iterator = iter(iterable)
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    return count
if __name__ == '__main__':
    sample_string = "hello"
    print(f"Counting elements in '{sample_string}': {count_elements(sample_string)}")
    sample_list = [1, 2, 3, 4, 5]
    print(f"Counting elements in {sample_list}: {count_elements(sample_list)}")
    sample_empty = ""
    print(f"Counting elements in '{sample_empty}': {count_elements(sample_empty)}")
    sample_list_empty = []
    print(f"Counting elements in {sample_list_empty}: {count_elements(sample_list_empty)}")