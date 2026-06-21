MAX_REVERSE_LENGTH = 1000

def reverse_generator(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if len(lst) > MAX_REVERSE_LENGTH:
        raise ValueError("List is too long to reverse in memory")
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    for item in reverse_generator(sample_list):
        print(item)