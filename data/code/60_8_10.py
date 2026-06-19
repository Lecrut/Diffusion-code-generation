def get_last_element(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        last_item = get_last_element(sample_list)
        print(f"The last item in the list {sample_list} is: {last_item}")
    except ValueError as e:
        print(e)