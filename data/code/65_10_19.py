def get_sublist(lst):
    try:
        return lst[2:5]
    except TypeError:
        return "Invalid input: Please provide a list."

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_sublist(sample_list)
    print(result)